from urllib import request
from django.urls import path, include
from . import views
from .views import *
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'upload', UploadViewSet, basename="upload")

urlpatterns= [

    path('college/', views.CollegeView.as_view(), name='college'),
    path('subject/', views.SubjectView.as_view(), name='subject'),
    path('student/', views.StudentView.as_view(), name='student'),    
    path('',views.FE.as_view(), name='FE'),
    path('upload/', include(router.urls)),
    
]
