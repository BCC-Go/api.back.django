from django.db import models

class User(models.Model):
    id = models.AutoField(
        primary_key=True,
        unique=True,
        editable=False,
        verbose_name="pk",
    )
    rank_id = models.CharField(
        max_length=2,
        null=False,
        default=1,
    )
    login_id = models.CharField(
        max_length=15,
        verbose_name="로그인 id",
    )
    name = models.CharField(
        max_length=5,
        verbose_name="이름",
    )
    password = models.CharField(
        max_length=40,
        null=False,
        verbose_name="비밀번호",
    )
    phone = models.CharField(
        unique=True,
        max_length=15,
        verbose_name="전화번호",
    )
    sex = models.CharField(
        max_length=2,
        null=False,
        verbose_name="성별",
    )
    birth = models.CharField(
        max_length=8,
        null=False,
        verbose_name="생년월일",
    )
    consumption = models.IntegerField(default=0,verbose_name="누적소비액",)
    address = models.CharField(
        max_length=100,
        null=False,
        verbose_name="주소",
    )
    type = models.CharField(max_length=2,default=0,verbose_name="소비자,판매자 타입")


