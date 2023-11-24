from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'galery/index.html')
# Create your views here.

def imagem(request):
    return render(request, 'galery/imagem.html')