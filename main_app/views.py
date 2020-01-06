from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Wig

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
    return render(request, 'wigs/detail.html', { 'wig': wig })