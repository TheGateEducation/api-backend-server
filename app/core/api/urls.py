from django.urls import path
from core.api.views import WelcomeView

urlpatterns = [
    path('', WelcomeView.as_view(), name='welcome'),
]
