from django.shortcuts import render
#está importando a classe HttpResponse do pacote django.shortcuts do framework Django.
from django.shortcuts import HttpResponse

# Create your views here.


def home(request):
    return render(request,'home/index.html')

def contato(request):
    return render(request,'contato/contact.html')