from django import http
from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib import auth
# Create your views here.
def sign_up(request):
    context = {}
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        password_check = request.POST.get('password_check')
        if (username and password and password == password_check):
            try:    
                new_user = User.objects.create_user(username=username, password=password)
                auth.login(request, new_user)
                print('로그인성공')
                return redirect('blog:home')
            except:
                context['error'] = '이미 존재하는 아이디입니다.'
        
        else:
            context['error'] = '아이디와 비밀번호를 잘못 입력하셨어요'
    return render(request, 'my_accounts/sign_up.html', context)

def login(request):
    if request.user.is_authenticated:
        return redirect('blog_samples:home') # 세션 아이디 저장돼서 get 방식으로 url 호출해도 계속 로그인 상태 되어있다.
    context = {}
    if request.method == 'POST': #요청이 POST인지 확인
        username = request.POST.get('username') #아이디 입력 받은 것 있어?  ㅇㅇ 
        password = request.POST.get('password') # 비밀번호 입력 받은 거 있어?  ㅇㅇ
        if (username and password):
            user = auth.authenticate(request, username=username, password=password) # 비밀번호 체크 
            if user is not None:
                auth.login(request, user)
                return redirect('blog_samples:home')
            else:
                context['error'] = '아이디와 비밀번호를 잘못 입력하셨어요'
        else:
            context['error'] = '아이디와 비밀번호를 입력해주세요'
    return render(request, 'my_accounts/login.html', context)

def logout(request):
    auth.logout(request)
    return redirect('blog_samples:home')

def naver_test(request):
    return render(request, "my_accounts/naver_test.html")