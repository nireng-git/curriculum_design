from  django.http import  HttpResponse
from django.shortcuts import redirect,reverse

def index(request):
    username = request.GET.get('username')
    if username:
        return HttpResponse("首页")
    else:
        # login_url = reverse('front:login')+"?next=/"
        login_url = reverse('front:detail',kwargs={"article_id":1,"p":4})
        print("="*50)
        return redirect(login_url)

def login(request):
    return HttpResponse('前台登录首页')

def article_detail(request,article_id,p):
    text = "您要查看的文章详情id是：%s, 第%s页"%(article_id,p)
    return HttpResponse(text)


