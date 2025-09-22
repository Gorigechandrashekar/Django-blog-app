from django.urls import path
from . import views

urlpatterns = [
    path('', views.save_user_name, name='save_user_name'),
    path('success/', views.success, name='success'),
]
