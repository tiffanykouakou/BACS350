from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def homePageView(request):
    return HttpResponse('Hello World')
    return HttpResponse('<h1>Hello There</h1><p>This is cool.</p>')
    return HttpResponse('<h1>This is a test</h1>" '<p>I'm trying to think but nothing happens</p>')
