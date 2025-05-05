from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path("user/",views.home,name="home"),
    path("",views.logouthome,name="logouthome")
   
]