from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class Profile(models.Model):
    # 프로필과 유저 객체를 하나씩 연결해준다!
    # 연결된 유저가 없어질때 CASCADE -> 프로필도 없어지도록
    # related_name 쉽게 연결할수 있게 도와줌
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')

    image = models.ImageField(upload_to='profile/', null=True)
    nickname = models.CharField(max_length=20, unique=True, null=True)
    message = models.CharField(max_length=100, null=True)
