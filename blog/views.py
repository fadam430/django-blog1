from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def my_blog_view(request):
    return HttpResponse("Welcome to my blog!")