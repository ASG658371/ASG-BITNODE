from rest_framework.response import Response
from rest_framework.views import APIView
from playground.models import *
from .serializers import *

class CollegesView(APIView):
   
    def get(self, request, pk=None):
        items=Colleges.objects.all()
        serializer = CollegesSerializer(items, many=True)
        return Response(serializer.data)

    
    def post(self, request):
        serializer = CollegesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()    
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
    
    # def update(self, request, pk):
    #     item = Colleges.objects.get(id=pk)
    #     serializer = CollegesSerializer(instance=item, data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()    
    #         return Response("Update Successful\n"+serializer.data)
    #     else:
    #         return Response("Error Occured while updating\n"+serializer.errors) 
    
    def delete(self, request, pk):
        item = Colleges.objects.get(colleges_id=pk)
        item.delete()
        return Response("Item Successfully Deleted")
    
    
    


# Create your views here.
