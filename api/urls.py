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

    path('colleges/<str:pk>', views.CollegesView.as_view(), name='colleges')
]
# urlpatterns = format_suffix_patterns(urlpatterns)