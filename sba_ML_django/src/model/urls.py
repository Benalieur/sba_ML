from django.contrib import admin
from django.urls import path

from .views import model, contact

urlpatterns = [
    path('', model, name="model"),
    path('contact', contact, name="contact"),
]
