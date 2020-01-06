from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Wig, Type, Photo
from .forms import ConditionForm
import uuid
import boto3

S3_BASE_URL = 'https://s3-us-east-2.amazonaws.com/'
BUCKET = 'wigcollector'

class WigCreate(LoginRequiredMixin, CreateView):
  model = Wig
  fields = ['name', 'origin', 'description', 'length']

  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)

class WigUpdate(LoginRequiredMixin, UpdateView):
  model = Wig
  fields = ['origin', 'description', 'length']

class WigDelete(LoginRequiredMixin, DeleteView):
  model = Wig
  success_url = '/wigs/'


# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

@login_required
def wigs_index(request):
    wigs = Wig.objects.filter(user=request.user)
    return render(request, 'wigs/index.html', { 'wigs': wigs})

@login_required
def wigs_detail(request, wig_id):
    wig = Wig.objects.get(id=wig_id)
    types_wig_doesnt_have = Type.objects.exclude(id__in = wig.types.all().values_list('id'))
    condition_form = ConditionForm()
    return render(request, 'wigs/detail.html', { 
        'wig': wig, 'condition_form': condition_form,
        'types': types_wig_doesnt_have 
    })

@login_required
def add_condition(request, wig_id):
	# create the ModelForm using the data in request.POST
    form = ConditionForm(request.POST)
  # validate the form
    if form.is_valid():
    # don't save the form to the db until it
    # has the cat_id assigned
        new_condition = form.save(commit=False)
        new_condition.wig_id = wig_id
        new_condition.save()
    return redirect('detail', wig_id=wig_id)

@login_required
def assoc_type(request, wig_id, type_id):
  Wig.objects.get(id=wig_id).types.add(type_id)
  return redirect('detail', wig_id=wig_id)

@login_required
def unassoc_type(request, wig_id, type_id):
  Wig.objects.get(id=wig_id).types.remove(type_id)
  return redirect('detail', wig_id=wig_id)

class TypeList(LoginRequiredMixin, ListView):
    model = Type

class TypeDetail(LoginRequiredMixin, DetailView):
    model = Type

class TypeCreate(LoginRequiredMixin, CreateView):
    model = Type
    fields = '__all__'

class TypeUpdate(UpdateView):
    model = Type
    fields = ['part', 'make']

class TypeDelete(LoginRequiredMixin, DeleteView):
    model = Type
    success_url = '/types/'

@login_required
def add_photo(request, wig_id):
    # photo-file will be the "name" attribute on the <input type="file">
    photo_file = request.FILES.get('photo-file', None)
    if photo_file:
        s3 = boto3.client('s3')
        # need a unique "key" for S3 / needs image file extension too
        key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
        # just in case something goes wrong
        try:
            s3.upload_fileobj(photo_file, BUCKET, key)
            # build the full url string
            url = f"{S3_BASE_URL}{BUCKET}/{key}"
            # we can assign to cat_id or cat (if you have a cat object)
            photo = Photo(url=url, wig_id=wig_id)
            photo.save()
        except:
            print('An error occurred uploading file to S3')
    return redirect('detail', wig_id=wig_id)

def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
    if form.is_valid():
        user = form.save()
        login(request, user)
        return redirect('index')
    else:
        error_message = 'Invalid sign up - try again'
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)