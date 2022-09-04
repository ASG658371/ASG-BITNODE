from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.
# request -> response
# request handler
# views
from django.http import HttpResponse

# def say_hello(request):
#     #pull data from DB
#     #Transform data
#     #send email
#     #return HttpResponse('Hello World') # Will send a string response on the page
#     return render(request, 'hello.html', {'name': 'Arpit'}) # Will send a template response on the page.

def upload(request):
    return render(request, 'upload.html')