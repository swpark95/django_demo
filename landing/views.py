from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

# Create your views here.


def index(request):
    context ={
        'weather' : "맑음",
        'temperature' : "17도"

    }
    return render(request, "index.html",context)


def months(request, month):
    month_list = []
    try:
        for i in range(1, 13):
            month_list.append(f"{i}월")
        return HttpResponse(month_list[month - 1])
    except:
        return HttpResponseNotFound('잘못된 요청입니다.')


def detail(request, name):
    users = [
        {"name": "hooni", "email": "hooni@naver.com", "hobby": "running"},
        {"name": "mina", "email": "mina@naver.com", "hobby": "dance"},
        {"name": "yami", "email": "yami@naver.com", "hobby": "reading"},
        {"name": "cool", "email": "cool@naver.com", "hobby": "surfing"},
        {"name": "jack", "email": "jack@naver.com", "hobby": "golf"},
    ]

    # result = ""
    a_user = None
    for user in users:
        if user["name"] == name:
            # result += f"<h1>{user['name']}, <h1><h2>{user['email']}, <h2><h3>{user['hobby']}<h3>"
            a_user = user
            # {"name": "hooni", "email": "hooni@naver.com", "hobby": "running"}
            break
    return render(request, "landing/users.html", a_user)

