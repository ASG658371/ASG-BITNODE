from django.urls import path
from . import views

#URLconf
urlpatterns = [
        path('upload/',views.upload, name='upload'),
]