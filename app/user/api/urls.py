"""User API routing endpoints"""
from django.urls import path, include
from user.api import views

urlpatterns = [
    path('create/', views.CreateUserView.as_view(), name='create-user'),
    path('me/', views.ManageUserView.as_view(), name='manage-user'),
]