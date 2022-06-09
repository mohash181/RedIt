from django.shortcuts import render
from .models import Post


def homeview(request):
    rposts = Post.objects.all()
    return render(request, "home.html", {"rposts":rposts})


def jsview(request):
    return render(request, "JStutorial.html")

def new_postview(request):
    pass
# Create your views here.
