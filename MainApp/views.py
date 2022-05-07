from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect, reverse, HttpResponse
from MainApp.models import StuInfo, TecInfo, PasswordResetToken, QuestionInfo
from StudentMessage.models import StuBasicInfo


def login(request):
    if 'login' in request.session and request.session['login']:
        return redirect(reverse('main:index'))
    if request.method == 'GET':
        context = {
            'base_url': request.build_absolute_uri('/main/password/front/')
        }
        return render(request, 'main/login.html', context)
    elif request.method == 'POST':
        username = request.POST.get('username')
        password_input = request.POST.get('password')
        role = int(request.POST.get('role'))
        try:
            if role == 1:
                # 学生
                user_object = StuInfo.objects.get(studentNo=username)
                password = user_object.password
            else:
                # 教职工
                user_object = TecInfo.objects.get(teacherNo=username)
                password = user_object.password
            if password_input == password:
                request.session['login'] = True
                request.session['username'] = username
                request.session['role'] = role
                # 登陆成功
                return redirect(reverse('main:index'))
            else:
                return HttpResponse('密码错误！')
        except ObjectDoesNotExist:
            return HttpResponse('用户不存在！')
    else:
        return HttpResponse('不支持的访问方法！')


def forget_password_set_role(request, username, role):
    """
    开始忘记密码之前设置role值
    """
    if request.method == 'GET':
        request.session['role'] = role
        return redirect(reverse('main:forget_password', args=[username]))
    else:
        return HttpResponse('不支持POST访问！')


def index(request):
    if 'login' not in request.session or not request.session['login']:
        return redirect(reverse('main:login'))

    if request.method == 'GET':
        role = int(request.session['role'])
        username = request.session['username']
        if role == 1:
            # 学生
            student = StuBasicInfo.objects.get(studentNo=username)
            request.session['studentName'] = student.studentName
            return render(request, 'main/index_student.html')
        elif role == 2:
            # 老师
            return redirect(reverse('student:baseinfo'))
            # return redirect('/student/baseinfo')
    else:
        return HttpResponse('不支持POST请求！')


def forget_password(request, username):
    try:
        if request.session['role'] == 1:
            user_object = StuInfo.objects.get(studentNo=username)
        else:
            user_object = TecInfo.objects.get(teacherNo=username)
    except ObjectDoesNotExist:
        return HttpResponse('用户不存在！')

    if user_object.email == '' and user_object.questionNo is None:
        return redirect(reverse('main:set_new_question', args=[username]))
    context = {
        'email': user_object.email,
        'question': user_object.questionNo,
        'username': username
    }
    return render(request, 'main/password/choose_method.html', context)


def forget_password_question(request, username):
    try:
        if int(request.session['role']) == 1:
            user_object = StuInfo.objects.get(studentNo=username)
        else:
            user_object = TecInfo.objects.get(teacherNo=username)
    except ObjectDoesNotExist:
        return HttpResponse('用户不存在！')

    if request.method == 'GET':

        context = {
            'question': user_object.questionNo.question,
            'username': username
        }
        return render(request, 'main/password/question.html', context)
    else:
        answer = request.POST.get('answer')
        new_password = request.POST.get('new_password')
        real_answer = user_object.answer
        if real_answer == answer:
            # 密保答案正确
            user_object.password = new_password
            user_object.save()
            return HttpResponse('密码修改成功！')
        else:
            # 密保答案错误
            return HttpResponse('密保答案错误！')


def set_new_password_email(request, token):
    try:
        token_object = PasswordResetToken.objects.get(token=token)
    except ObjectDoesNotExist:
        return HttpResponse('Token不存在！')

    if request.method == 'GET':
        return render(request, 'main/password/set_new_password_email.html', {'token': token})
    else:
        user_object = token_object.student if token_object.student is not None else token_object.teacher
        new_password = request.POST.get('new_password')
        user_object.password = new_password
        user_object.save()
        # 删除Toke
        token_object.delete()
        return HttpResponse('密码修改成功！')


def logout(request):
    if 'login' in request.session and request.session['login']:
        request.session['login'] = False
    return redirect(reverse('main:login'))


def render_static_html(request, path):
    response = render(request, 'main/' + path)
    response['X-Frame-Options'] = 'sameorigin'
    return response


def set_user_question(request, username):
    if request.method == 'GET':
        question_objects = QuestionInfo.objects.all()
        return render(request, 'main/password/set_question.html', {'username': username, 'questions': question_objects})
    else:
        question_id = request.POST.get('question_id')
        answer = request.POST.get('answer')
        if request.session['role'] == 1:
            user_object = StuInfo.objects.get(studentNo=username)
        else:
            user_object = TecInfo.objects.get(teacherNo=username)
        # 这里判断身份证后六位是否正确，但是表中没有身份证字段
        question_object = QuestionInfo.objects.get(questionNo=question_id)
        user_object.questionNo = question_object
        user_object.answer = answer
        user_object.save()
        return redirect(reverse('main:index'))
        #return redirect(reverse('main:forget_password', args=[username]))


def index_redirect(request):
    return redirect(reverse('main:index'))
