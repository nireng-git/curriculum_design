"""orm_relationship URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from book import views as book_view
from article import views as article_view

urlpatterns = [
    path('',book_view.index,name='index'),
    path('article/',article_view.index,name='article'),
    path('one_many/',article_view.one_to_many_view,name='one_many'),
    path('one_one/',article_view.one_to_one_view,name='one_one'),
    path('many_many/',article_view.many_to_many_view,name='many_many'),
]
