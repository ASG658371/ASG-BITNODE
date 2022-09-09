from django.urls import path
from . import views

#URLconf
urlpatterns = [
        path('',views.FE.as_view(), name='FE'),
]