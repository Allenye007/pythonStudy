from django.shortcuts import render
import uuid
import csv
# Create your views here.
from django.http import HttpResponse,StreamingHttpResponse,JsonResponse


def index(request):
    return HttpResponse("allen")


def write_csv(request):
    req = request.POST.dict()
    uid = uuid.uuid1()
    list = [uid]
    for item in req:
        list.append(req[item])
    # newline='' 删掉隔行的空格
    with open("static/data.csv", "a", encoding='GBK', newline='') as f:
        writer = csv.writer(f)
        res = writer.writerow(list)
        return JsonResponse(
            {
                "errorCode": 0,
                # "data": request.POST
            }
        )

def read_csv(request):
    with open("static/data.csv", 'r', encoding='GBK') as f:
        row = csv.reader(f, delimiter = ',')
        next(row)
        list = []
        for r in row:
            obj = {}
            obj['uid'] = r[0]
            obj['name'] = r[1]
            obj['age'] = r[2]
            obj['sex'] = r[3]
            obj['vip'] = r[4]
            obj['tel'] = r[5]
            list.append(obj)
        return JsonResponse(
            {
                "list": list
            }
        )
