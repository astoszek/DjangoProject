import datetime

from django.shortcuts import HttpResponse
from django.shortcuts import render

# Create your views here.

def hello_world(request):
    return HttpResponse("Hello world, From Django!")

def current_time(request):
    return HttpResponse(f'Czas wywołania widoku: {datetime.datetime.now()}')

wywolania_licznik = 0

def licznik_view(request):
    global wywolania_licznik
    wywolania_licznik += 1
    return HttpResponse(f'Ta ścieżka została wywołana {wywolania_licznik} razy.')