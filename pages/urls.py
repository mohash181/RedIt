from django.urls import path
from .views import *

app_name = "pages"

urlpatterns = [
    path("home/", homeview, name="home"),
    path("new_post/", new_postview, name="new_post"),
    path("js/", jsview, name="javascript")
]