from django.http import HttpResponse
from django.shortcuts import render
from .models import Jobs

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
        "jobs": jobs
    })    