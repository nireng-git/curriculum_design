from django.shortcuts import render
from django.http import HttpResponse
from .models import Article,Category,Tag
from frontuser.models import FrontUser
# Create your views here.
def index(request):
    # category = Category(name="伦理")
    # category.save()
    # article = Article(title="毕业季",content="希望不要留太多遗憾")
    # article.category = category
    # article.save()
    article = Article.objects.first()
    print(article.category.name)
    return HttpResponse("SUCCESS")

def one_to_many_view(request):
    users = FrontUser(username="kangbazi")
    users.save()
    article = Article(title="钢铁是怎样弄断的", content="abc")
    category = Category.objects.first()
    article.category = category
    article.author = users
    article.save()
    return HttpResponse("SUCCESS")