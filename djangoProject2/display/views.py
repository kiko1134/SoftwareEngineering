from django.shortcuts import render
import requests

def index(request):
    response = requests.get('https://api.covid19api.com/countries').json()
    return render(request, 'index.html', {'response':response})


# Create your views here.
