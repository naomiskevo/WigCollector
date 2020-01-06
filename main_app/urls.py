from django.urls import  path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('wigs/', views.wigs_index, name='index'),
    path('wigs/<int:wig_id>/', views.wigs_detail, name='detail'),
    path('wigs/create/', views.WigCreate.as_view(), name='wigs_create'),
    path('wigs/<int:pk>/update/', views.WigUpdate.as_view(), name='wigs_update'),
    path('wigs/<int:pk>/delete/', views.WigDelete.as_view(), name='wigs_delete'),
    path('wigs/<int:wig_id>/add_condition/', views.add_condition, name='add_condition'),
]
