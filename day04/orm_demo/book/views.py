from django.shortcuts import render
from django.http import  HttpResponse
from .models import Book
# Create your views here.
# class Person(object):
#     username = 'ad'
#     age = 18
#     height='181cm'
#
#
#  p = Person()
#
# person
#     id  username  age  height
#     1   kangbazi    18 181cm
#     2   test        20  191

def index(request):
    #添加
    # book = Book(name="mysql从删库到跑路",author="扛把子",price=100.1)
    # book.save()

    # 查询
    # book = Book.objects.get(pk=1)
    # book = Book.objects.filter(name="mysql从删库到跑路").first()
#     # print(book)
#     # return HttpResponse("查询成功")

    # book = Book.objects.get(pk=1)
    # book.delete()
    book = Book.objects.get(pk=2)
    book.price = 200
    book.save()
    return HttpResponse("更新成功")