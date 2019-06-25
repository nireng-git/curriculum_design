from django.shortcuts import render
from .models import Book, BookOrder, Publisher, Author
from django.http import HttpResponse
from django.db.models import Avg, Count, Max, Min, Sum, F, Q
from django.db import connection


# Create your views here.
def index(request):
    result = Book.objects.aggregate(avg=Avg("price"))
    print(result)
    # print(result.query) #只有filter才可以使用query
    print(connection.queries)
    return HttpResponse("获取所有图书的平均价")


def index1(request):
    # 每一本书销售的平均价格
    result = Book.objects.aggregate(avg=Avg("bookorder__price"))
    print(result)
    print(connection.queries)

    print("==" * 50)
    books = Book.objects.annotate(avg=Avg("bookorder__price"))
    for book in books:
        print("%s:%s" % (book.name, book.avg))
    print(connection.queries)
    return HttpResponse("每一本书销售的平均价格")


def index3(request):
    # book表中总共多少本书，作者表中总共多少不同的邮箱
    # books = Book.objects.aggregate(booknums=Count("id"))
    # print(books)

    # author = Author.objects.aggregate(email_nums=Count('email', distinct=True))
    # print(author)
    # print(connection.queries)

    books = Book.objects.annotate(book_numbers=Count("bookorder"))
    for book in books:
        print("%s:%s"%(book.name,book.book_numbers))
    print(connection.queries)
    return HttpResponse("book表中总共多少本书")

def index4():
    pass
