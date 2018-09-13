from django.http import HttpResponse
from django.shortcuts import resirect


def index(request):
    return HttpResponse("index")
