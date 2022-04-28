from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Post
from django.urls import reverse
# Create your views here.

def index(request):
    return HttpResponse('<h1>Hello, Django!</h1>')

def post_write(request):
    if request.method == "GET": 
        return render(request,"blog/create.html")
    elif request.method == "POST": # 입력받은 데이터를 받아서 처리해야 할 때
        new_post = Post()
        new_post.title = request.POST["title"] # request.POST 가 도대체 뭐냐? django 기본 문법이다. 참고 https://docs.djangoproject.com/en/4.0/ref/request-response/
        new_post.content = request.POST["content"]
        if request.FILES.get("image"): #get 함수를 써서 key error 방지
            new_post.head_image = request.FILES.get("image")
        new_post.save()
        return HttpResponseRedirect(reverse("blog:home"))

def blog_home(request):
    blog_posts = Post.objects.all()
    context = {
        'blog_posts_key':blog_posts
    }
    return render(request, 'blog/index.html', context)

def post_detail(request, post_id):
    post = Post.objects.get(id=post_id)
    context = {
            'post_id':post.id,
            'post_title':post.title,
            'post_content':post.content,
    }
    print(post.head_image.url)
    if post.head_image:
        context['post_image'] = post.head_image
    return render(request, 'blog/detail.html', context)

def post_update(request, post_id):
    post = Post.objects.get(id=post_id)
    if request.method == "GET":
        context = {
            'post_id':post.id,
            'post_title':post.title,
            'post_content':post.content,
        }
        a = reverse("blog:detail", args=[post.id])
        return render(request, 'blog/edit.html', context)
    elif request.method == "POST":
        post.title = request.POST["title"] #input tag의 name이 "title"인 것을 받아서 post.title에 저장
        post.content = request.POST["content"] #input tag의 name이 "content"인 것을 받아서 post.content에 저장
        post.save()
        return HttpResponseRedirect(f'/blog/post-detail/{post.id}/')


def post_delete(request, post_id):
    if request.method == "POST":
        post = Post.objects.get(id=post_id)
        post.delete()
        return HttpResponseRedirect(reverse("blog:home"))


