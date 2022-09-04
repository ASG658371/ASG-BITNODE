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
    path('subject/', views.SubjectView.as_view(), name='subject'),
    path('student/', views.StudentView.as_view(), name='student'),    
]
# urlpatterns = format_suffix_patterns(urlpatterns)