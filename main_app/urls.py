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
    path('wigs/<int:wig_id>/add_photo/', views.add_photo, name='add_photo'),
    path('types/', views.TypeList.as_view(), name='types_index'),
    path('types/<int:pk>/', views.TypeDetail.as_view(), name='types_detail'),
    path('types/create/', views.TypeCreate.as_view(), name='types_create'),
    path('types/<int:pk>/update/', views.TypeUpdate.as_view(), name='types_update'),
    path('types/<int:pk>/delete/', views.TypeDelete.as_view(), name='types_delete'),
    path('accounts/signup/', views.signup, name='signup'),
    path('wigs/<int:wig_id>/assoc_type/<int:type_id>/', views.assoc_type, name='assoc_type'),
    path('wigs/<int:wig_id>/unassoc_type/<int:type_id>/', views.unassoc_type, name='unassoc_type'),
]
