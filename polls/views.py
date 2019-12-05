from django.shortcuts import render

# Create your views here.
# -*- coding: utf-8 -*-
from django.http import HttpResponse
import urllib.request
import urllib
from .models import Question

def read (request):
    # 1、网址url  --百度
    url = 'http://www.baidu.com'

    # 2、创建request请求对象
    request = urllib.request.Request(url)

    # 3、发送请求获取结果
    response = urllib.request.urlopen(request)
    htmldata = response.read()

    # 4、设置编码方式
    htmldata = htmldata.decode('utf-8')

    # 5、打印结果
    # print(htmldata)

    # 6、打印爬去网页的各类信息
    # print("response的类型:", type(response))
    # print("请求的url:", response.geturl())
    # print("响应的信息:", response.info())
    # print("状态码:", response.getcode())

    # 7、爬取数据保存到文件
    fileOb = open('1.html', 'w', encoding='utf-8')
    fileOb.write(htmldata)
    fileOb.close()
    return HttpResponse(htmldata)


def first (request):
    latest_question_list = Question.objects.order_by('-pub_date')[:4]
    output = ', '.join([q.question_text for q in latest_question_list])
    return HttpResponse(output)

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def add_ques(request):
    # if (request.method == "POST"):
    #     print(request["name"], "响应了")
    data = request.GET['name']
    return HttpResponse(data)
