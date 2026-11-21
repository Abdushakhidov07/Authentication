from django.urls import path, include
from .views import *

urlpatterns = [
    path("registration/", registration, name="registration"),
    path("profile/", profile, name="profile"),
    path("login/", login_user, name="login"),
    path("logout/", logout_user, name="logout"),   
    path("create_task/", create_task, name="create_task"),
    path("show_task/", show_task, name="my_task"),
    path('show_task_id/<int:pk>', show_task_by_id, name='show_task_by_id'),
    path('choice_status/<int:pk>', change_status, name='choice_status')
    
]
