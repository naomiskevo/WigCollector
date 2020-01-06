from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import Wig

class WigCreate(CreateView):
  model = Wig
  fields = ['name', 'origin', 'description', 'length']

  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)


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