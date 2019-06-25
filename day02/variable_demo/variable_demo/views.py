from django.shortcuts import render

class Person(object):
    def __init__(self,username):
        self.username = username

def index(request):
    p = Person('CXX')

    # context = {
    #     'person':p
    # }

    # context = {
    #     'person':{
    #         'username':'yangdan'
    #     }
    #}

    # context = {
    #     'person': (
    #         '啊哈  cxx',
    #         'fj',
    #         'cd',
    #     )
    # }

    # context = {
    #     'age':16
    # }

    # context = {
    #     'heros':[
    #         '乔丹',
    #         '科比',
    #         '詹姆斯',
    #     ]
    # }

    # context = {
    #     'persons':{
    #         'username':'cxk',
    #         'age':18,
    #         'height':'171cm'
    #     }
    # }

    # context = {
    #     'persons': {
    #         'username': 'cxk',
    #         'age': 18,
    #         'height': '171cm'
    #     }
    # }

    # context = {
    #     'comments':[
    #         '你打球像cxk'
    #     ],
    #     'books':[
    #         {
    #             'name':'python深入浅出',
    #             'author':'扛把子',
    #             'price':200
    #         },
    #         {
    #             'name': 'mysql从入门到放弃',
    #             'author': '扛把子1',
    #             'price': 100
    #         },
    #         {
    #             'name': 'python深入浅出',
    #             'author': '扛把子2',
    #             'price': 200
    #         },
    #         {
    #             'name': 'python深入浅出',
    #             'author': '扛把子3',
    #             'price': 200
    #         },
    #         {
    #             'name': 'JavaScript十年刚刚入门',
    #             'author': '扛把子4',
    #             'price': 180
    #         },
    #     ]
    # }

    context = {
        'persons':[
            '张三',
            '李四',
            '王五'
        ]
    }

    return render(request,'index.html',context=context)
    # return render(request,'index.html',context={'username':"dddddd"})
