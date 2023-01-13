from django.urls import path
from . import views
from django.contrib import admin

urlpatterns = [
    path('', views.index, name='home'),
    path('landing/' , views.landing, name='landing'),
    path('<str:job_id>' , views.jobs, name='jobs')
    
]
