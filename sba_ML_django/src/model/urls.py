from django.contrib import admin
from django.urls import path

from .views import model

urlpatterns = [
    path('', model, name="model"),
]
