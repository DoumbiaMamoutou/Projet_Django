from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'pages/architectures/index.html')


def about_architec(request):
    return render(request, 'pages/architectures/abouts.html')

def project_architec(request):
    return render(request, 'pages/architectures/project.html')

def single_architec(request):
    return render(request, 'pages/architectures/single_project.html')

def service_architec(request):
    return render(request, 'pages/architectures/services.html')