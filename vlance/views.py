from django.http import HttpResponse
from django.shortcuts import render
from .models import Jobs

# Create your views here.
def index(request):
    return render(request, "vlance/index.html", {
        "jobs": Jobs.objects.all()
    })
def landing(request):
    return render(request, "app/landing.html")