from django.http import HttpResponse
from djang.cutshort import redicert


def index(request):
    return HttpResponse("index")
