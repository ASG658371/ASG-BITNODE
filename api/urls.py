from django.urls import path
from . import views
from api.views import HelloWorldView
urlpatterns = [
    path('',HelloWorldView.as_view()),
]