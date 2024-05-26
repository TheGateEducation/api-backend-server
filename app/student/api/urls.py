"""Student API URL Configuration"""
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from student.api import views

router = DefaultRouter()
router.register('records', views.StudentRecordViewSet)

urlpatterns = [
    path('', include(router.urls)),
]