from django.contrib import admin
from django.urls import include,path
from . import views
urlpatterns=[
    path("admin/",admin.site.urls),
    path("",views.main,name="main"),
    path("members/",views.members,name='members'),
    path("members/details/<int:id>",views.details,name="details"),
]