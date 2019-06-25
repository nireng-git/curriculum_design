import requests

def send(mobile,captcha):
    url = 'http://v.juhe.cn/sms/send'
    params ={
        "mobile":mobile, #手机号  必须传
        "tpl_id":"135629", #模板的id
        "tpl_value":"#code#="+captcha,
        "key":"",

    }
    response = requests.get(url,params=params)
    result = response.json()
    print(result)

    if result['error_code'] == 0 :
        return True
    else:
        return False


send(13888888888,'888889')
