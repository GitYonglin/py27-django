# _*_ coding: utf-8 _*_

from datetime import  datetime

from django.db import models
from django.contrib.auth.models import AbstractUser #用于数据的继承

# Create your models here.


class UserProfile(AbstractUser): # 继承原来的user数据model
    nick_name = models.CharField(max_length=50,verbose_name='昵称',default="")
    birday = models.DateField(verbose_name=u'生日',null=True)
    gender = models.CharField(choices=(("male","男"),('female',"女")),default='male',max_length=6, verbose_name="性别")
    address = models.CharField(max_length=200,default="",null=True, verbose_name="地址")
    phone = models.CharField(max_length=11, null=True,blank=True, verbose_name="手机号码")
    image = models.ImageField(upload_to="image/%Y/%m", default=u"image/default.png", max_length=100, verbose_name="头像")

    class Meta:
        verbose_name= "用户"
        verbose_name_plural = verbose_name

    def __unicode__(self): #重载这个方法 扩展时需要重写
        return self.username


class EmailVerifyRecord(models.Model): #邮箱验证码
    code = models.CharField(max_length=20, verbose_name="验证码")
    email = models.CharField(max_length=50, verbose_name="邮箱")
    send_type = models.CharField(max_length=8, choices=(("register","注册"),("forget","找回密码")),verbose_name="类型")
    send_time = models.DateTimeField(default=datetime.now, verbose_name="创建时间") #这时间不要加 ()

    class Meta:
        verbose_name = "邮箱验证码"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.code


class Banner(models.Model):
    title = models.CharField(max_length=50, verbose_name="标题")
    image = models.ImageField(upload_to="banner/%Y/%m",verbose_name="轮播图", max_length=100)
    url = models.URLField(max_length=100, verbose_name="访问地址")
    index = models.BigIntegerField(default=100, verbose_name="顺序")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "轮播图"
        verbose_name_plural = verbose_name














