from django.shortcuts import render

# Create your views here.


def inscription(request):
    return render(request, 'pages/utilisateur/inscription.html')