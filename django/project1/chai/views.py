from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from .models import chaiVariety
# Create your views here.
def chai(request):
    chai_list = chaiVariety.objects.all()
    return render(request, 'layout.html', {'chai_list': chai_list})
def about(request):
    return HttpResponse("Hello,You are at Django about page.")

def contact(request):
    return HttpResponse("Hello,You are at Django Contact page.")


