from django.urls import path

from . import views

urlpatterns = [
    path('',views.createHome, name='home')
]