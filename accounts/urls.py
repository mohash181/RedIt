from django.urls import path
from .views import *


app_name = "accounts"


urlpatterns = [
    path("signup/", signupview, name="signup"),
    path("login/", loginview, name="login"),
    path("logout/", logoutview, name="logout"),
    path("loggedout/", loggedoutview, name="loggedout")
]