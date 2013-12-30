# from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("You are at /gradebook.")

def downloads(request):
    return HttpResponse("You are at /downloads.")
