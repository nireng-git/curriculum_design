from django.shortcuts import render
from datetime import datetime
# Create your views here.

def index(request):
    context = {
        'mytime':datetime(year=2019,month=6,day=13,hour=9,minute=25,second=10)
    }
    return render(request,'index.html',context=context)

