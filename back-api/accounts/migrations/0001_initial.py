# Generated by Django 3.2.13 on 2022-04-17 08:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(editable=False, primary_key=True, serialize=False, unique=True, verbose_name='pk')),
                ('rank_id', models.CharField(default=1, max_length=2)),
                ('login_id', models.CharField(max_length=15, verbose_name='로그인 id')),
                ('name', models.CharField(max_length=5, verbose_name='이름')),
                ('password', models.CharField(max_length=40, verbose_name='비밀번호')),
                ('phone', models.CharField(max_length=15, unique=True, verbose_name='전화번호')),
                ('sex', models.CharField(max_length=2, verbose_name='성별')),
                ('birth', models.CharField(max_length=8, verbose_name='생년월일')),
                ('consumption', models.IntegerField(default=0, verbose_name='누적소비액')),
                ('address', models.CharField(max_length=100, verbose_name='주소')),
                ('type', models.CharField(default=0, max_length=2, verbose_name='소비자,판매자 타입')),
            ],
        ),
    ]
