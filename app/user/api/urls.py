"""User API routing endpoints"""

from django.urls import include, path
from rest_framework import routers

from user.api import views

app_name = 'user'

urlpatterns = [
    path('api/create/', views.CreateUserView.as_view(), name='create'),
    path("api/me/", views.ManageUserView.as_view(), name = "me")
]