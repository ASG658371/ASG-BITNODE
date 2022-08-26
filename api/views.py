from rest_framework.response import Response
from rest_framework.views import APIView
from playground.models import test
from .serializers import testSerializer

class HelloWorldView(APIView):
   
   def get(self, request):
    items=test.objects.all()
    serializer = testSerializer(items, many=True)
    return Response(serializer.data)

   def post(self, request):
    serializer = testSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()    
    return Response(serializer.data)


# Create your views here.
