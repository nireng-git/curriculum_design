from django.shortcuts import render
from .models import Article,Category,Tag
from django.http import HttpResponse
from frontuser.models import FrontUser,UserExtension
# Create your views here.

def index(request):
    # category = Category(name="伦理动作")
    # category.save()
    # article = Article(title="人生苦短,我用python",content="java100行代码，python可能只需要五行")
    # article.category =category
    # article.save()
    # article = Article.objects.first()
    # print(article.category.name)
    return HttpResponse("成功")

def one_to_many_view(request):
    # article = Article(title="论屌丝的逆袭",content="我一点也不想你，一点半再想")
    # category = Category.objects.first()
    # frontUser = FrontUser(username="kangbazi")
    # frontUser.save()
    # article.category = category
    # article.author = frontUser
    # article.save()
    # return HttpResponse("成功")
    #获取分类下面所有的文章
    # category = Category.objects.first()
    # article = category.article_set.first() #当你在外键 不写,related_name="articles" 使用模型的小写_set 获取 一下面所有的多
    # print(article)
    # category = Category.objects.first()
    # articles = category.articles.all()#articles 就是我们在model中写的related_name
    # for article in  articles:
    #     print(article)
    category = Category.objects.first()
    article = Article(title="三国演义",content="既生瑜何生亮")
    article.author = FrontUser.objects.first()
    category.articles.add(article,bulk=False)
    #自动的保存article不需要在添加category之前先保存article
    #不需要额外的保存一次了
    return HttpResponse("成功")

def one_to_one_view(request):
    # user = FrontUser.objects.get(pk=2)
    # extension = UserExtension(school='南昌大学')
    # extension.user = user
    # extension.save()
    # extension = UserExtension.objects.first()
    # print(extension.user)
    user = FrontUser.objects.get(pk=2)
    print(user.extension.school)
    return HttpResponse("一对一成功")


def many_to_many_view(request):
    # article = Article.objects.first()
    # tag = Tag(name="人设崩塌")
    # tag.save()
    # article.tags.add(tag)

    #添加标签的两种方式
    # tag = Tag.objects.first()
    # article = Article.objects.get(pk=3)
    # tag.articles.add(article)

    article = Article.objects.get(pk=3)
    tags = article.tags.all()
    for tag in  tags:
        print(tag)
    return HttpResponse("多对多成功")