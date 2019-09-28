from django.shortcuts import render

# Create your views here.

def blog_home(request):
    return render(request, 'pages/blog/accueil_blog.html')

def single_blog(request):
    return render(request, 'pages/blog/single_blog.html')