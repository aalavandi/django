from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    # return HttpResponse("Hello,You are at Django home page.")
    return render(request,'website/index.html')

def about(request):
    return HttpResponse("Hello,You are at Django about page.")

def contact(request):
    return HttpResponse("Hello,You are at Django Contact page.")