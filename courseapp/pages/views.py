from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home(request):
    return HttpResponse('anasayfa')

def hakkimizda(request):
    return HttpResponse('hakkimizda')

def iletisim(request):
    return HttpResponse('iletisim')
