from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def home(request):
    
    message = request.GET.get("message")

    print(message)

    return render(request,"home.html")