from urllib import request
from rest_framework.urlpatterns import format_suffix_patterns
from django.urls import path
from . import views
from api.views import *
from rest_framework.routers import DefaultRouter

# router = DefaultRouter()

# router.register(r'', views.CollegesView, basename='colleges')

# urlpatterns = router.urls
urlpatterns= [

    path('college/', views.CollegeView.as_view(), name='college'),
    path('college/<str:pk>/', views.CollegeView.as_view(), name='college')
    
]
# urlpatterns = format_suffix_patterns(urlpatterns)