from http.client import HTTP_PORT, HTTPResponse
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.





def profile(request):
    return render(request,'employee/profile.html')