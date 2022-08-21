import imp
from urllib import request
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView

class HelloWorldView(APIView):
   
   def get(self, request):
    output_dict={"message":"Hello World"}
    return Response(output_dict)

   def post(self, request):
    name=request.data['name']
    return Response({'message':'Hi'+name})


# Create your views here.
