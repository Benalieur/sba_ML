from django.shortcuts import render
from datetime import datetime as dt

def index(request):

    return render(request, "sba_ML_django/index.html")