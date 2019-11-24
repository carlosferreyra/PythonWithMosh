from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

# products -> index
# Uniform resourse Locator (Address)


def index(request):
    return HttpResponse("Hello World")
