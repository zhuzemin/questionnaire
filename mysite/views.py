import datetime
from django.shortcuts import render

def current_datetime(request):
    now = datetime.datetime.now()
    return render(request,'current_datetime.html',{'current_date': now})

