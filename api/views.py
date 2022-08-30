from rest_framework.response import Response
from rest_framework.views import APIView
from playground.models import *
from .serializers import *

class CollegeView(APIView):
    
    def get(self, request, pk=None):
        if pk == None:
            items=College.objects.all()
            serializer = CollegeSerializer(items, many=True)
            return Response(serializer.data)
        else:
            items=College.objects.get(college_id=pk)
            serializer = CollegeSerializer(items, many=False)
            return Response(serializer.data)
    
    def post(self, request, pk=None):
        serializer = CollegeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()    
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
    
    def patch(self, request, pk):
        item = College.objects.get(college_id=pk)
        serializer = CollegeSerializer(instance=item, data=request.data)
        if serializer.is_valid():
            serializer.save()    
            return Response("Update Successful")
        else:
            return Response("Error Occured while updating") 
    
    def delete(self, request, pk):
        item = College.objects.get(college_id=pk)
        item.delete()
        return Response("Item Successfully Deleted")
    
    
    


# Create your views here.
