from django.urls import  path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('wigs/', views.wigs_index, name='index'),
    path('wigs/<int:wig_id>/', views.wigs_detail, name='detail'),
    path('wigs/create/', views.WigCreate.as_view(), name='wigs_create'),
]
