from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm

def homeview(request):
    rposts = Post.objects.all()
    return render(request, "home.html", {"rposts":rposts})


def jsview(request):
    return render(request, "JStutorial.html")

def new_postview(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            username = request.user
            title = form.cleaned_data.get("title")
            text = form.cleaned_data.get("text")
            draft = True if request.POST.get("draft") else False
            publish = True if request.POST.get("publish") else False
            newpost = Post(user=username, title=title, text=text, draft=draft,published=publish)
            newpost.save()
            newpost.publish()
            return redirect("pages:home")
        else:
            return render(request, "create.html", {"form":form})
    else:
        form = PostForm()
        return render(request, "create.html", {"form":form})
                    
# Create your views here.
