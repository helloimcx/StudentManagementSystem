# -*- coding: utf-8 -*-

from django.contrib import admin
from django.urls import path, include, re_path

from StudentMessage.views import StudentBaseView, StuModifyInfoView, StudentSearchView, \
    StudentModifyP, StudentModifyEmail, TeacherBaseView, StuDetailView, StudentAdd

app_name = 'student'
urlpatterns = [
    #学生基本信息
    path('baseinfo/', StudentBaseView.as_view(), name='baseinfo'),
    # 学生密码修改
    path('modifypassworld/', StudentModifyP.as_view(), name='modifypassworld'),
    # 学生有限个修改
    path('modifyemail/', StudentModifyEmail.as_view(), name='modifyemail'),
    #修改个人信息
    path('modifyinfo/', StuModifyInfoView.as_view(), name='modifyinfo'),
    #学生信息查询
    path('searchinfo/', StudentSearchView.as_view(), name='searchinfo'),
    # 教师信息查询
    path('teacherinfo/', TeacherBaseView.as_view(), name='teacherinfo'),
    #学生详细信息
    path('studetail/', StuDetailView.as_view(), name="studetail"),
    # 学生基本信息添加
    path('stuadd/', StudentAdd.as_view(), name="stuadd"),



]
