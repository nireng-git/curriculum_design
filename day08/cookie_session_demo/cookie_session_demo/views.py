from django.http import HttpResponse
from datetime import datetime
from django.utils.timezone import make_aware

def index(request):
    #key cookie的key
    #value cookie的值
    #max_age 最长的声明周期 单位是秒
    #expires  过期时间  同时设置了 max_age 和 expires 以expires 为基准
    #path 对域名下的哪个路径有效
    #domain 针对哪个域名有效
    #secure 是否是安全的 如果为true 只能是https协议的
    #httponly 如果为true 只能通过页面访问  不能通过ajax
    response = HttpResponse('index')
    expires = datetime(year=2019,month=6,day=22,hour=20,minute=30,second=40)
    expires = make_aware(expires)
    response.set_cookie('user_id','shuaizhou',expires=expires,max_age=180,path='/cms/')

    return response

def delete_cookie(request):
    response = HttpResponse('delete')
    response.delete_cookie('user_id')
    return response

def cms_view(request):
    cookies = request.COOKIES
    username = cookies.get('user_id')
    return HttpResponse(username)

def my_view(request):
    cookies = request.COOKIES
    username = cookies.get('user_id')
    return HttpResponse(username)

from datetime import timedelta
def session_view(request):
    # expires = datetime(year=2019, month=6, day=22, hour=20, minute=30, second=40)
    # expires = make_aware(expires)

    request.session['username']= 'kangbazi'
    request.session['age']= 18
    # expiry = timedelta(days=3)
    # request.session.set_expiry(None)
    # request.session.set_expiry(0)
    expiry = timedelta(days=2)
    request.session.set_expiry(expiry)
    return HttpResponse("SESSION VIEW")

def get_session(request):
    username = request.session.get('username')
    print(username)
    return HttpResponse("GET SESSION VIEW")

def log_out(request):
    request.session.clear_expired()
    return HttpResponse("清空过期的session")