from django.shortcuts import render

# Create your views here.

def index(request):
    context = {
        "username":"kangbazi"
    }
    return render(request,'index.html',context=context)

def company(request):
    return render(request, 'company.html')

def school(request):
    return render(request, 'school.html')