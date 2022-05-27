from django.urls import path
from .views import *

urlpatterns = [
    path("home/", homeview, name="home"),
    path("new_post/", new_postview, name="new_post")
]