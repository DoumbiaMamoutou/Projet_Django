from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('about/', views.about_architec, name="abouts"),
    path('architec/', views.project_architec, name="project_architec"),
    path('single/', views.single_architec, name="single_architec"),
    path('service/', views.service_architec, name="service_architec"),
    
]
