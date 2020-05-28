from django.shortcuts import render

# Create your views here.
from django.http import Http404
from django.shortcuts import render

def home_view(request):
    return render(request, 'home.html')