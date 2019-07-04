from django.shortcuts import render
from django.http import HttpResponse

def index(request):
	return HttpResponse("Hello, my friend!")

# Create your views here.
