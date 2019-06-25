from django.shortcuts import render
from .models import Article,Category,Tag
from frontuser.models import FrontUser
from django.http import HttpResponse
from frontuser.models import UserExtension
# Create your views here.
def index(request):
    # category = Category(name="最火文章")
    # category.save()
    # article = Article(title="你这么可爱",content="我是不会还回去的")
    # article.category = category
    # article.save()
    article = Article.objects.first()
    print(article.category.name)
    return HttpResponse("SUCCESS")

def one_to_many_view(request):
    # article = Article(title="你不珍惜我，告诉你", content="我是不会还回去的")
    # category = Category.objects.first()
    # author = FrontUser(username="kangbazi")
    # author.save()
    # article.author = author
    # article.save()

    # 获取分类下面所有的文章
    # category = Category.objects.first()
    # articles = category.article_set.all()
    # for article in articles:
    #     print(article)

    # category = Category.objects.first()
    # articles = category.articles.all()   #related_name
    # for article in articles:
    #     print(article)

    category = Category.objects.first()
    article = Article(title="我可以抱你吗",content="j呱唧呱唧")
    article.author = FrontUser.objects.first()

    #bluk=False的作用是不需要额外的保存article，直接添加就可以了
    category.articles.add(article,bluk=False)
    return HttpResponse("一对多SUCCESS")

def one_to_one_view(request):
    # user = FrontUser.objects.first()
    # extension = UserExtension(school="五道口职业学院")
    # extension.user = user
    # extension.save()
    extension = UserExtension.objects.first()
    print(extension.user)

    user = FrontUser.objects.first()
    # print(user.extension.all)
    extension = user.extension
    print(extension)
    return HttpResponse("一对一SUCCESS")

def many_to_many_view(request):
    # article = Article.objects.first()
    # tag = Tag(name="人生苦短，我用python")
    # tag.save()
    # article.tag_set.add(tag)

    # article = Article.objects.first()
    # tag = Tag(name="python搜素指数绝对第一")
    # tag.save()
    # article.tags.add(tag)

    # tag = Tag.objects.get(pk=2)
    # article = Article.objects.get(pk=3)
    # tag.articles.add(article)

    #标签下面的文章
    article = Article.objects.get(pk=1)
    tags = article.tags.all()
    for tag in tags:
        print(tag)
    return HttpResponse("多对多成功")
