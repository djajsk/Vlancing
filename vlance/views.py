from django.http import HttpResponse , HttpResponseRedirect
from django.shortcuts import render
from .models import Jobs
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse

# Create your views here.
def index(request):
    return render(request, "vlance/index.html", {
        "jobs": Jobs.objects.all()
    })
def landing(request):
    return render(request, "vlance/landing.html")

def jobs(request, job_id):
    jobs = Jobs.objects.get(id=job_id)
    return render(request, "vlance/job.html", {
        "jobs": jobs,
        "works": Jobs.objects.all()
    })    

def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request , username = username , password = password)
        if username is not None:
            login(request , user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request , "vlance/login.html" , {
                "message" : "Invalid Credentials"
            })
    else:
        return render(request, "vlance/login.html")        

def logout_view(request):
    logout(request)
    return render(request, "vlance/landing.html")
         