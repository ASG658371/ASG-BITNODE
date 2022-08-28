from rest_framework.response import Response
from rest_framework.views import APIView
from playground.models import *
from .serializers import CollegeSerializer

class HelloWorldView(APIView):
   
   def get(self, request):
    items=Colleges.objects.all()
    serializer = CollegeSerializer(items, many=True)
    return Response(serializer.data)

   def post(self, request):
    serializer = CollegeSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()    
        return Response(serializer.data)
    else:
        return Response(serializer.errors)


# Create your views here.
