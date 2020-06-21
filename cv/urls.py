from django.urls import path
from . import views

urlpatterns = [
    path('cv/', views.cv_home, name='cv_home'),
    path('cv/edit/basic-information', views.edit_basic_information, name='edit_basic_information'),
]