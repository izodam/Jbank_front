# accounts_models.py
from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    nickname = models.CharField(max_length=255, blank=True, null=True)  # 닉네임 정보 추가
    age = models.IntegerField(null=True, blank=True)        # 나이 정보 추가
    money = models.IntegerField(null=True, blank=True)      # 자산 정보 추가
    salary = models.IntegerField(null=True, blank=True)     # 연봉 정보 추가

class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    prdt_type = models.TextField()  # 'deposit' or 'saving'
    fin_prdt_cd = models.TextField()
    fin_prdt_nm = models.TextField()
    kor_co_nm = models.TextField()
