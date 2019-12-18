from django.shortcuts import render
from .models import Wig


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