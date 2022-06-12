from django.urls import path
from .views import *

app_name = "pages"

urlpatterns = [
    path("home/", homeview, name="home"),
    path("create/", new_postview, name="create"),
    path("js/", jsview, name="javascript")
]