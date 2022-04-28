from distutils.command.upload import upload
from django.db import models

# Create your models here.

#class 테이블 이름 (models.Model 상속 받는다):
class Post(models.Model):
    #클래스 변수# 
    title = models.CharField(max_length=100)
    content = models.TextField()
    head_image = models.ImageField(upload_to='blog/images/%Y/%m/%d/%H', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True) # 처음 데이터가 추가될 때 시간을 자동으로 입력
    updated_at = models.DateTimeField(auto_now=True) # 데이터가 갱신될 떄 시간을 자동으로 입력

    def __str__(self):
        return f'제목:{self.title}, 내용:{self.content}'