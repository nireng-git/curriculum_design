from django.shortcuts import render,redirect,reverse
from .models import Article
from django.http import HttpResponse

# Create your views here.


def index(request):
    return HttpResponse("首页")

def add_article(request):
    if request.method == 'GET':
        return render(request,'add_article.html')
    else:
        title = request.POST.get('title')
        content = request.POST.get('content')
        price = request.POST.get('price')
        Article.objects.create(title=title,content=content,price=price)
        return redirect(reverse('index'))