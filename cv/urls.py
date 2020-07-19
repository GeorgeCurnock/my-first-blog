from django.urls import path
from . import views

urlpatterns = [
    path('cv/', views.cv_home, name='cv_home'),
    path('cv/edit/basic', views.cv_edit_basic, name='cv_edit_basic'),
    path('cv/new/education', views.cv_new_education, name='cv_new_education'),
    path('cv/edit/education/<int:pk>/', views.cv_edit_education, name='cv_edit_education'),
    path('cv/new/experience/', views.cv_new_experience, name='cv_new_experience'),
    path('cv/edit/experience/<int:pk>/', views.cv_edit_experience, name='cv_edit_experience'),
    path('cv/new/projects/', views.cv_new_projects, name='cv_new_project'),
    path('cv/edit/projects/<int:pk>/', views.cv_edit_projects, name='cv_edit_project'),
    path('cv/edit/skills/', views.cv_edit_skills, name='cv_edit_skills'),
]