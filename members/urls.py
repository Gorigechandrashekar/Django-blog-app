from django.contrib import admin
from django.urls import include,path
from . import views
urlpatterns=[
    path("",include('users.urls')),
    path("",views.main,name="main"),
    path("members/",views.members,name='members'),
    path("members/details/<slug:slug>",views.details,name="details"),
]