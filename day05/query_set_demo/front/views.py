from django.shortcuts import render
from django.http import HttpResponse
from .models import Book,Article,Category
from datetime import datetime
from django.utils.timezone import make_aware
# Create your views here.

def index(request):
    print(type(Book.objects))
    return HttpResponse("index")

def index1(request):
    # book = Book.objects.filter(name__exact="千锋发展史")
    book = Book.objects.filter(name__iexact="千锋发展史")
    print(book.query)
    print(book)

    return HttpResponse("index1")

def index2(request):
    book = Book.objects.filter(name__contains="千锋")
    print(book.query)
    print(book)

    return HttpResponse("index2")

def index3(request):
    articles = Article.objects.filter(id__in=[1,2,3,4])
    for article in  articles:
        print(article)


    categorys = Category.objects.filter(articles__in=[1,2,3,4])
    for category in categorys:
        print(categorys)
    print(categorys.query)
    return HttpResponse("index3")

def index4(request):
    articles = Article.objects.filter(id__gte=2)
    for article in articles:
        print(article)
    print(articles.query)
    return HttpResponse("index4")

def index5(request):
    articles = Article.objects.filter(id__gte=2)
    for article in articles:
        print(article)
    print(articles.query)
    return HttpResponse("index4")

def index6(request):
    start_time = make_aware(datetime(year=2019,month=1,day=6,hour=12,minute=13,second=14))
    end_time = make_aware(datetime(year=2019,month=7,day=6,hour=12,minute=13,second=14))
    articles = Article.objects.filter(create_time__range=(start_time,end_time))
    print(articles.query)
    print(articles)
    return HttpResponse("index6")

def index7(request):
    #文章中包含"千锋的" 分类是？
    categories = Category.objects.filter(articles__title__contains="千锋")
    for categorie in categories:
        print(categorie)
    print(categories.query)
    return HttpResponse("index7")