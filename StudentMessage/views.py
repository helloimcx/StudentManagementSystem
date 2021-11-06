# -*- coding:utf-8 -*-
import datetime
import json

from django.http import QueryDict
from django.shortcuts import render
from django.views.generic.base import View

from MainApp.models import StuInfo
from StudentMessage.models import StuBasicInfo,ClassInfo
from django.http import HttpResponse


# 学生基本信息
class StudentBaseView(View):
    def get(self, request):
        username = request.session['username']
        role = request.session['role']
        if role==1:
            try:
                Stuinfo = StuBasicInfo.objects.get(studentNo=username)
            except Exception as e:
                Stuinfo = []
            return render(request, 'main/files/Student/std_BasicInfo.html', {'Stuinfo': Stuinfo})
        else:
            try:

                classinfo=ClassInfo.objects.get(teacherNo=username)

                Stuinfo_list=classinfo.cla.all()
            except Exception as e:
                Stuinfo = []

            return render(request, 'main/files/teacher/class_basicInfo.html',
                              {"Stuinfo_list": Stuinfo_list, "classinfo": classinfo})


#学生信息修改
class StuModifyInfoView(View):

    def get(self, request):

        username = request.session['username']
        role = request.session['role']

        if role==1:
            try:
                Stuinfo = StuBasicInfo.objects.get(studentNo=username)
            except Exception as e:
                Stuinfo = []
        elif role==2:
            pass

        else:
            pass

        return render(request, 'main/files/Student/std_ModifyInfo.html', {'Stuinfo': Stuinfo})

    def post(self, request):
        username = request.session['username']
        IdentityNum=request.POST.get("IdentityNum")
        PersonalTele=request.POST.get("PersonalTele")
        mobilePhone=request.POST.get("mobilePhone")
        photo=request.FILES.get("photo")
        Family=request.POST.get("Family")
        FamilyLocation=request.POST.get("FamilyLocation")
        FamilyTele=request.POST.get("FamilyTele")
        Stuinfo = StuBasicInfo.objects.get(studentNo=username)
        Stuinfo.email=IdentityNum
        Stuinfo.bankcard=PersonalTele
        Stuinfo.telephone=mobilePhone
        if photo is not None:
            Stuinfo.photo=photo
        Stuinfo.family=Family
        Stuinfo.address=FamilyLocation
        Stuinfo.fphone=FamilyTele
        Stuinfo.save()
        return HttpResponse(u"修改成功")


#学生信息查询
class StudentSearchView(View):
    def get(self, request):
        username = request.session['username']
        role = request.session['role']
        args=QueryDict(request.GET.get("data"))
        college=args.get("college")
        major=args.get("major")
        cclass=args.get("class")
        condition=args.get("condition")
        sort=request.GET.get("rank")
        Stuinfo = StuBasicInfo.objects.filter().all()

        try:
            classinfo = ClassInfo.objects.get(teacherNo=username)

            Stuinfo_list = classinfo.cla.all()

            if sort == 'asc':
                Stuinfo_list = Stuinfo_list.order_by('studentNo')
            else:
                Stuinfo_list = Stuinfo_list.order_by('-studentNo')
            if condition:
                Stuinfo_list=Stuinfo_list.filter(studentNo=condition).all()
        except Exception as e:
            Stuinfo = []
        return render(request, 'main/files/teacher/class_basicInfo.html',{"Stuinfo_list":Stuinfo_list,"classinfo":classinfo})

#学生密码修改
class StudentModifyP(View):
    def get(self, request):

        username = request.session['username']
        role = request.session['role']

        if role == 1:
            try:
                Stuinfo = StuBasicInfo.objects.get(studentNo=username)
            except Exception as e:
                Stuinfo = []
            return render(request, 'main/files/Student/std_ModifyPassword.html', {'Stuinfo': Stuinfo})
    def post(self, request):
        username = request.session['username']
        data=QueryDict(request.POST.get("data"))
        newPassword = data.get("newPassword")
        confirmPassword = data.get("confirmPassword")
        if newPassword !=confirmPassword:
            return HttpResponse({"status":"fail", "msg":"密码不一致！"}, content_type='application/json')
        else:
            Stuinfo = StuInfo.objects.get(studentNo=username)
            Stuinfo.password = newPassword
            Stuinfo.save()
            return HttpResponse('{"status":"success","msg": "修改成功！"}', content_type='application/json')

# 学生邮箱修改
class StudentModifyEmail(View):
    def get(self, request):

        username = request.session['username']
        role = request.session['role']

        if role == 1:
            try:
                Stuinfo = StuBasicInfo.objects.get(studentNo=username)
            except Exception as e:
                Stuinfo = []
        return render(request, 'main/files/Student/std_ModifyEmail.html', {'Stuinfo': Stuinfo})

    def post(self, request):
        username = request.session['username']
        newEmail = request.POST.get("newEmail")

        stuinfo = StuBasicInfo.objects.get(studentNo=username)
        s_obj=StuInfo.objects.get(studentNo=username)

        stuinfo.email = newEmail
        stuinfo.save()
        s_obj.email=newEmail
        s_obj.save()
        return HttpResponse('{"status":"success","msg": "修改成功！"}', content_type='application/json')


#教师基本信息
class TeacherBaseView(View):
    def get(self, request):
        username = request.session['username']
        role = request.session['role']
        if role == 3:
            return render(request, 'main/files/university/sch_studentBasicInfo.html')
        else:
            return render(request, 'main/files/university/sch_teacherBasicInfo.html')
    def post(self, request):
        pass

#学生详细信息查询
class StuDetailView(View):
    def get(self, request):
        stuno=request.GET.get("data")
        Stuinfo = StuBasicInfo.objects.filter(studentNo=stuno).first()
        return render(request, 'main/files/Student/detail.html',{"Stuinfo":Stuinfo})
    def post(self,request):
        data=QueryDict(request.POST.get("data"))
        sno=data.get("studentNo")
        Stuinfo = StuBasicInfo.objects.filter(studentNo=sno).first()
        is_delete = request.POST.get("is_delete", False)
        if is_delete:
            Stuinfo.delete()
            return HttpResponse('{"status":"success","msg": "删除成功！"}', content_type='application/json')
        political = data.get("political")
        eduBackground = data.get("eduBackground")
        telephone = data.get("telephone")
        bankcard = data.get("bankcard")
        family = data.get("family")
        address = data.get("address")
        englishlevel = data.get("englishlevel")
        fmaily_phone = data.get('family_phone')
        id_card = data.get('id_card')
        email = data.get('email')
        hometown = data.get('hometown')
        nation = data.get('nation')
        college = data.get('college')
        major = data.get('major')
        class_name = data.get('class_name')
        sex = data.get('sex')
        student_name = data.get('student_name')
        Stuinfo.political = political
        Stuinfo.eduBackground = eduBackground
        Stuinfo.telephone = telephone
        Stuinfo.family = family
        Stuinfo.address = address
        Stuinfo.bankcard = bankcard
        Stuinfo.englishlevel=englishlevel
        Stuinfo.fphone = fmaily_phone
        Stuinfo.idcard = id_card
        Stuinfo.email = email
        Stuinfo.hometown = hometown
        Stuinfo.nation = nation
        Stuinfo.college = college
        Stuinfo.major = major
        Stuinfo.ClassName = class_name
        Stuinfo.sex = 1 if sex == "男" else 0
        Stuinfo.studentName = student_name
        Stuinfo.save()
        return HttpResponse('{"status":"success","msg": "修改成功！"}', content_type='application/json')



#学生基本信息添加
class StudentAdd(View):
    def post(self,request):
        data= json.loads(request.POST.get("datats"))
        for obj in data:
            ct=ClassInfo.objects.first()
            try:
                sf=StuInfo.objects.get(studentNo=obj[0])
            except:
                sf=StuInfo()
                sf.studentNo=obj[0]
                sf.save()
            sno = obj[0]
            sname =  obj[1]
            profession =  obj[2]
            classname = obj[3]
            sex =  obj[4]
            nation =  obj[5]
            birthPlace =  obj[6]
            political =  obj[7]
            IDCard =  obj[8]
            schooling =  obj[9]
            cete = obj[10]
            job =  obj[11]
            bandCard =  obj[12]
            stuinfo = StuBasicInfo()
            stuinfo.studentNo=sf
            stuinfo.ClassNo=ct
            stuinfo.studentName=sname
            stuinfo.major=profession
            stuinfo.ClassName=classname
            stuinfo.sex=sex
            stuinfo.nation=nation
            stuinfo.hometown=birthPlace
            stuinfo.political=political
            stuinfo.idcard=IDCard
            stuinfo.eduBackground=schooling
            stuinfo.englishlevel=cete
            stuinfo.bankcard=bandCard
            stuinfo.remarks=job
            stuinfo.birthday=datetime.datetime.now()
            stuinfo.save()
        return HttpResponse('{"status":"success","msg": "11！"}', content_type='application/json')

