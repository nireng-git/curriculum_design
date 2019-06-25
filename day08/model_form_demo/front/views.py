from django.shortcuts import render
from django.http import HttpResponse
from .forms import AddBookForm
from .models import Book

# Create your views here.

def add_book(request):
    form = AddBookForm(request.POST)
    if form.is_valid():
        title = form.cleaned_data.get('title')
        page = form.cleaned_data.get('page')
        price = form.cleaned_data.get('price')

        print("title:%s" %title)
        print("page:%s" %page)
        print("price:%s" %price)
        form.save()

        return HttpResponse("success")
    else:
        print(form.errors.get_json_data())
        return HttpResponse("fail")