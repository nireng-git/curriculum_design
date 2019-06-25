from django.shortcuts import render
from django.http import HttpResponse
from .models import Book
# Create your views here.
def index(request):
    #添加数据
    # book = Book(name="金什么梅",author="笑笑生",price=12.3)
    # book.save()

    #查询数据
    #根据主键查找
    # book = Book.objects.get(pk=6)
    # print(book)

    # books = Book.objects.filter(name='金什么梅').all()
    # for book in  books:
    #     print(book)

    # books = Book.objects.filter(name='金什么梅').first()
    # print(books)

    # book = Book.objects.get(pk=5)
    # book.price = 666
    # book.save()
    # book = Book.objects.get(pk=4)
    # book.delete()


    return HttpResponse("成功")

