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