from rest_framework.response import Response
from rest_framework.views import APIView
from playground.models import *
from .serializers import *

class CollegeView(APIView):
    
    def get(self, request):
            clg=College.objects.all()
            serializer = CollegeSerializer(clg, many=True)
            return Response(serializer.data)
           
    def post(self, request):
        serializer = CollegeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()    
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
    
    def patch(self, request):
        pk=request.query_params['pk']
        clg = College.objects.get(pk=pk)
        serializer = CollegeSerializer(instance=clg, data=request.data)
        if serializer.is_valid():
            serializer.save()    
            return Response(serializer.data)
        else:
            return Response(serializer.errors) 
    
    def delete(self, request):
        pk = request.query_params['pk']
        clg = College.objects.get(pk=pk)
        if not clg:
            return Response("Item does not exist")
        else:
            clg.delete()
            return Response("Item Successfully Deleted")

class SubjectView(APIView):
    def get(self, request):
        pk=request.query_params['pk']
        if pk == None:
            subj=Subject.objects.all()
            serializer = SubjectSerializer(subj, many=True)
            return Response(serializer.data)
        else:
            subj=Subject.objects.get(pk=pk)
            serializer = SubjectSerializer(subj, many=False)
            return Response(serializer.data)
    
    def post(self, request):
        serializer = SubjectSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()    
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
    
    def patch(self, request):
        pk=request.query_params['pk']
        subj = Subject.objects.get(pk=pk)
        serializer = SubjectSerializer(instance=subj, data=request.data)
        if serializer.is_valid():
            serializer.save()    
            return Response(serializer.data)
        else:
            return Response(serializer.errors) 
    
    def delete(self, request):
        pk=request.query_params['pk']
        subj = Subject.objects.get(pk=pk)
        if not subj:
            return Response("Item does not exist")
        else:
            subj.delete()
            return Response("Item Successfully Deleted")


class StudentView(APIView):
    
    def get(self, request):
        pk=request.query_params['pk']
        if pk == None:
            stud=Student.objects.all()
            serializer = StudentSerializer(stud, many=True)
            return Response(serializer.data)
        else:
            stud=Student.objects.get(pk=pk)
            serializer = StudentSerializer(stud, many=False)
            return Response(serializer.data)
    
    def post(self, request):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()    
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
    
    def patch(self, request):
        pk=request.query_params['pk']
        stud = Student.objects.get(pk=pk)
        serializer = StudentSerializer(instance=stud, data=request.data)
        if serializer.is_valid():
            serializer.save()    
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
    
    def delete(self, request):
        pk=request.query_params['pk']
        stud = Student.objects.get(pk=pk)
        if not stud:
            return Response("Item does not exist")
        else:
            stud.delete()
            return Response("Item Successfully Deleted")

    
    
    


# Create your views here.
