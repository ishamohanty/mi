from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def ishu(request):
    return render(request,'ishu.html')
