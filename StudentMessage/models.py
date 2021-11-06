# -*- coding:utf-8 -*-
from django.db import models

from MainApp.models import StuInfo, TecInfo


class PoliticalStatus(models.Model):
    politicalNo = models.CharField(primary_key=True, max_length=8,verbose_name='政治面貌编码')
    politicalName = models.CharField(max_length=24, verbose_name='政治面貌编码')

    class Meta:
        verbose_name = '政治面貌表'
        verbose_name_plural = '政治面貌表'

    def __str__(self):
        return self.studentName


class DepInfo(models.Model):
    departNo = models.CharField(primary_key=True, max_length=4, verbose_name='部门编号')
    depart = models.CharField(max_length=36, verbose_name='部门名称')
    departBrief = models.CharField(max_length=27, verbose_name='部门简称')
    departInfo = models.CharField(max_length=90, verbose_name='部门描述')
    depNumber = models.IntegerField(default=0, verbose_name='人数')
    girlNumber = models.IntegerField(default=0,verbose_name='女生人数')
    freNumber = models.IntegerField(default=0,verbose_name='大一人数')
    sopNumber = models.IntegerField(default=0,verbose_name='大二人数')
    junNumber = models.IntegerField(default=0,verbose_name='大三人数')
    senNumber = models.IntegerField(default=0,verbose_name='大四人数')
    depState = models.BooleanField(verbose_name='状态',default=True)

    class Meta:
        verbose_name = '学院部门信息表'
        verbose_name_plural = '学院部门信息表'

    def __str__(self):
        return self.depart

class MajorInfo(models.Model):
    majorNo = models.CharField(primary_key=True, max_length=8, verbose_name='专业编号')
    major = models.CharField(max_length=60, verbose_name='专业方向')
    MajorShort = models.CharField(max_length=45, verbose_name='简称')
    departNo = models.CharField(max_length=4, verbose_name='部门编码')
    majorInfo = models.CharField(max_length=150, verbose_name='专业描述')
    marjorNumber = models.IntegerField(default=0,verbose_name='人数')
    majorState = models.BooleanField(verbose_name='状态',default=True)

    class Meta:
        verbose_name = '专业信息表'
        verbose_name_plural = '专业信息表'

    def __str__(self):
        return self.major

class ClassInfo(models.Model):
    classNo = models.CharField(primary_key=True, max_length=14, verbose_name='班级编号')
    className = models.CharField(max_length=45, verbose_name='班级名称')
    classBrief = models.CharField(max_length=30, verbose_name='班级简称')
    majorNo = models.ForeignKey(to=MajorInfo, on_delete=models.CASCADE, verbose_name='专业编号')
    classNumber = models.IntegerField(verbose_name='人数',default=0)
    girlNumber = models.IntegerField(verbose_name='女生人数',default=0)
    schoolDate = models.DateField(verbose_name='入学时间')
    studyTime = models.IntegerField(verbose_name='学制')
    classState = models.IntegerField(verbose_name='状态')
    teacherNo = models.ForeignKey(to=TecInfo, on_delete=models.CASCADE, verbose_name='老师编号')

    class Meta:
        verbose_name = '班级信息表'
        verbose_name_plural = '班级信息表'

    def __str__(self):
        return self.className




class StuBasicInfo(models.Model):
    studentNo = models.ForeignKey(to=StuInfo, on_delete=models.CASCADE, related_name="stu_stu",verbose_name='学号')
    studentName = models.CharField(max_length=18, verbose_name='姓名')
    birthday=models.DateTimeField(verbose_name='出生日期')
    ClassNo = models.ForeignKey(to=ClassInfo, on_delete=models.CASCADE, verbose_name='班级编号',related_name='cla')
    ClassName=models.CharField(max_length=30,verbose_name='班级')
    major=models.CharField(max_length=30,verbose_name='专业方向')
    college=models.CharField(max_length=30,verbose_name='学院')
    sex=models.IntegerField(verbose_name='性别')
    nation=models.CharField(max_length=30,verbose_name='名族')
    hometown=models.CharField(max_length=84,verbose_name='籍贯')
    political=models.CharField(max_length=24,verbose_name='政治面貌')
    idcard=models.CharField(max_length=18,verbose_name='身份证号')
    telephone=models.CharField(max_length=11,blank=True, null=True,verbose_name='手机号')
    email = models.CharField(max_length=50, blank=True, null=True, verbose_name='个人邮箱')
    emailOnly = models.IntegerField(verbose_name='邮箱绑定',default=0)
    family = models.CharField(max_length=30, blank=True, null=True,verbose_name='家庭联系人')
    address = models.CharField(max_length=60, blank=True, null=True,verbose_name='家庭地址')
    fphone = models.CharField(max_length=18, blank=True, null=True,verbose_name='家庭联系电话')
    photo = models.FileField(upload_to="media/",blank=True, null=True, verbose_name='照片')
    eduBackground = models.CharField(max_length=12, blank=True, null=True,verbose_name='学历')
    englishlevel = models.CharField(max_length=12, blank=True, null=True,verbose_name='英语等级')
    bankcard = models.CharField(max_length=25, blank=True, null=True, verbose_name='银行卡号')
    exameState = models.CharField(max_length=30, blank=True, null=True, verbose_name='审核状态')
    remarks = models.CharField(max_length=150, blank=True, null=True, verbose_name='备注')
    stuState = models.IntegerField(verbose_name='状态',default=1)

    class Meta:
        verbose_name = '学生基本信息表'
        verbose_name_plural = '学生基本信息表'

    def __str__(self):
        return self.studentName
