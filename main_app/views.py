from django.shortcuts import render
from django.http import HttpResponse

class Wig:
  def __init__(self, name, origin, description, length):
    self.name = name
    self.origin = origin
    self.description = description
    self.length = length

wigs = [
    Wig('Victoria', 'Brazilian', 'dark brown body wave', 22),
    Wig('Candace', 'Synthetic', 'rainbow blunt cut bob', 12),
    Wig('Gladys', 'Persian', 'black curly hair', 18),
]
# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def wigs_index(request):
    return render(request, 'wigs/index.html', { 'wigs': wigs})