from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import ConditionForm
import uuid
import boto3
from .models import Wig, Photo

S3_BASE_URL = 'https://s3-us-east-2.amazonaws.com/'
BUCKET = 'wigcollector'

class WigCreate(CreateView):
  model = Wig
  fields = ['name', 'origin', 'description', 'length']

  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)

class WigUpdate(UpdateView):
  model = Wig
  fields = ['origin', 'description', 'length']

class WigDelete(DeleteView):
  model = Wig
  success_url = '/wigs/'


# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def wigs_index(request):
    wigs = Wig.objects.all()
    return render(request, 'wigs/index.html', { 'wigs': wigs})

def wigs_detail(request, wig_id):
    wig = Wig.objects.get(id=wig_id)
    condition_form = ConditionForm()
    return render(request, 'wigs/detail.html', { 
        'wig': wig, 'condition_form': condition_form, 
    })

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