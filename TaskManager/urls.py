from django.urls import path, include
from .views import *

urlpatterns = [
    path("registration/", registration, name="registration"),
    path("profile/", profile, name="profile"),
    path("login/", login_user, name="login"),
    path("logout/", logout_user, name="logout"),   
    path("create_task/", create_task, name="create_task"),
    path("show_task/", show_task, name="my_task") 
]
