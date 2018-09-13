from django.http import HttpResponse
from djang.shortcuts import redicert


def index(request):
    return HttpResponse("index")
