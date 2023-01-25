from django.urls import path , include
from . import views
from django.contrib import admin

urlpatterns = [
    path('index/', views.index, name='index'),
    path('' , views.landing, name='landing'),
    path('<str:job_id>' , views.jobs, name='jobs'),
    path('login/', views.login_view, name='login'),
    path('logout', views.logout_view, name='logout')
    
]
