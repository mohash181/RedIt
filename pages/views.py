from django.shortcuts import render



def homeview(request):
    return render(request, "home.html")


def new_postview(request):
    pass
# Create your views here.
