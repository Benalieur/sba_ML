from django.shortcuts import render
from datetime import datetime as dt

def index(request):

    date = dt.today()

    context = {'date' : date}

    return render(request, "sba_ML_django/index.html", context=context)