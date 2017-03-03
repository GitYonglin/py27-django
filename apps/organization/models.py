# _*_ coding: utf-8 _*_

# 机构model
from datetime import  datetime

from django.db import models

# Create your models here.


class CityDict(models.Model):
    name = models.CharField(max_length=20, verbose_name=u"城市")
    desc = models.CharField(max_length=200, verbose_name=u"描述")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"")

    class Meta:
        verbose_name = u"城市"
        verbose_name_plural = verbose_name


class CourseOrg(models.Model):
    name = models.CharField(max_length=50,verbose_name=u"机构名称")
    desc = models.TextField(verbose_name=u"机构描述")
    click = models.IntegerField(default=0, verbose_name=u"点击量")
    fav_nums = models.IntegerField(default=0, verbose_name=u"收藏量")
    image = models.ImageField(upload_to="org/%Y/%m", verbose_name=u"封面")
    address = models.CharField(max_length=150, verbose_name=u"机构地址")

    class Meta:
        verbose_name = u"机构"
        verbose_name_plural = verbose_name


class Teacher(models.Model):
    org = models.ForeignKey(CourseOrg, verbose_name=u"所属机构")
    name = models.CharField(max_length=10,verbose_name=u"教师名字")
    work_years = models.IntegerField(default=0,verbose_name=u"工作年限")
    work_company = models.CharField(max_length=50, verbose_name=u"就职公司")
    work_position = models.CharField(max_length=50, verbose_name=u"职位")
    points = models.IntegerField(default=0, verbose_name=u"教学特点")
    click_nums = models.IntegerField(default=0, verbose_name=u"点击量")
    fav_nums = models.IntegerField(default=0, verbose_name=u"收藏量")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")


    class Meta:
        verbose_name = u"教师"
        verbose_name_plural = verbose_name































