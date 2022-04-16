from django.db import models

class User(models.Model):
    id = models.AutoField(
        primary_key=True,
        unique=True,
        editable=False,
        verbose_name="pk",
    )
    login_id = models.CharField(
        max_length=15,
        verbose_name="이름",
    )
    phone = models.CharField(
        unique=True,
        max_length=15,
        verbose_name="전화번호",
    )

