from django.http import HttpResponse
from django.shortcuts import render,redirect,reverse
from django.views.generic import View,TemplateView

def index(request):
    return HttpResponse("首页类视图")

class BookListView(View):
    def get(self,request,*args,**kwargs):
        return HttpResponse("book list view")

class AddBookView(View):
    def get(self,request,*args,**kwargs):
        return render(request,"add_book.html")

    def post(self, request, *args, **kwargs):
        book_name = request.POST.get("name")
        book_author = request.POST.get("author")
        print("name:{},author:{}".format(book_name,book_author))
        return HttpResponse("添加成功")

# class AboutView(TemplateView):
#     template_name = 'about.html'
#     def get_context_data(self, **kwargs):
#         context = {"phone":'23232'}
#         return context