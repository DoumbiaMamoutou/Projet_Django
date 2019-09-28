from django.urls import path

from . import views

urlpatterns = [
    path('', views.blog_home, name="blog"),
    path('singles', views.single_blog, name="single_blog"),

]