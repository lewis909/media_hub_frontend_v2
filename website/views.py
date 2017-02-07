from django.shortcuts import render

def index(request):
    return render(request, 'website/home.html')

def test2(request):
    return render(request, 'website/hom2.html')
