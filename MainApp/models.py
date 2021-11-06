from django.db import models


# Create your models here.
class QuestionInfo(models.Model):
    class Meta:
        verbose_name = '密保问题'
        verbose_name_plural = '密保问题'

    # 密保问题编号
    questionNo = models.IntegerField(primary_key=True, verbose_name='密保问题编号')

    # 密保问题
    question = models.CharField(max_length=30, blank=False, verbose_name='密保问题')

    def __str__(self):
        return self.question


class RoleInfo(models.Model):
    class Meta:
        verbose_name = '角色信息'
        verbose_name_plural = '角色信息'

    # 角色编号
    roleNo = models.IntegerField(primary_key=True, verbose_name='角色编号')

    # 角色名称
    roleName = models.CharField(max_length=45, blank=False, verbose_name='角色名称')

    # 创建时间
    createTime = models.DateField(blank=False, null=False, verbose_name='创建日期')

    # 角色描述
    roleDescription = models.TextField(blank=True, verbose_name='角色描述')

    def __str__(self):
        return self.roleName


class PurviewInfo(models.Model):
    class Meta:
        verbose_name = '权限信息'
        verbose_name_plural = '权限信息'

    # 编号
    id = models.IntegerField(primary_key=True, verbose_name='编号')

    # 上级权限编号
    pid = models.IntegerField(blank=True, verbose_name='上级权限编号')

    # 权限名称
    purviewName = models.CharField(max_length=45, blank=False, verbose_name='权限名称')

    # 权限请求
    purviewUrl = models.URLField(blank=True, verbose_name='权限请求')

    def __str__(self):
        return self.purviewName


class StuInfo(models.Model):
    class Meta:
        verbose_name = '学生信息'
        verbose_name_plural = '学生信息'

    # 学号
    studentNo = models.CharField(max_length=8, primary_key=True, verbose_name='学号')

    # 密码
    password = models.CharField(max_length=12, blank=False, verbose_name='密码')

    # 密保问题编号
    questionNo = models.ForeignKey(to=QuestionInfo, on_delete=models.DO_NOTHING, blank=True, null=True, verbose_name='密保问题')

    # 密保问题答案
    answer = models.CharField(max_length=30, blank=True, verbose_name='密保问题答案')

    # 状态
    stuStatus = models.BooleanField(default=True, blank=False, verbose_name='状态，是否为该校学生')

    # 邮箱
    email = models.CharField(max_length=128, blank=True, verbose_name='邮箱')

    def __str__(self):
        return self.studentNo


class TecInfo(models.Model):
    class Meta:
        verbose_name = '教师信息'
        verbose_name_plural = '教师信息'

    # 工号
    teacherNo = models.CharField(max_length=4, primary_key=True, verbose_name='工号')

    # 密码
    password = models.CharField(max_length=12, blank=False, verbose_name='密码')

    # 密保问题编号
    questionNo = models.ForeignKey(to=QuestionInfo, on_delete=models.DO_NOTHING, blank=True, null=True, verbose_name='密保问题编号')

    # 密保问题答案
    answer = models.CharField(max_length=30, blank=True, verbose_name='密保问题答案')

    # 在职状态
    tecStatus = models.BooleanField(default=True, blank=False, verbose_name='在职状态')

    # 邮箱
    email = models.CharField(max_length=128, blank=True, verbose_name='邮箱')

    def __str__(self):
        return self.teacherNo


class TeacherPurview(models.Model):
    class Meta:
        verbose_name = '教师权限关联'
        verbose_name_plural = '教师权限关联'

    # 教师编号
    teacherNo = models.ForeignKey(to=TecInfo, on_delete=models.CASCADE, verbose_name='教师编号')

    # 权限编号
    purviewNo = models.ForeignKey(to=PurviewInfo, on_delete=models.DO_NOTHING, verbose_name='权限编号')


class RolePurview(models.Model):
    class Meta:
        verbose_name = '角色权限关联'
        verbose_name_plural = '角色权限关联'

    # 角色编号
    roleNo = models.ForeignKey(to=RoleInfo, on_delete=models.CASCADE, verbose_name='角色编号')

    # 权限编号
    purviewNo = models.ForeignKey(to=PurviewInfo, on_delete=models.DO_NOTHING, verbose_name='权限编号')


class TeacherRole(models.Model):
    class Meta:
        verbose_name = '教师角色关联'
        verbose_name_plural = '教师角色关联'

    # 教师编号
    teacherNo = models.ForeignKey(to=TecInfo, on_delete=models.CASCADE, verbose_name='教师编号')

    # 角色编号
    roleNo = models.ForeignKey(to=RoleInfo, on_delete=models.DO_NOTHING, verbose_name='角色编号')


class PasswordResetToken(models.Model):
    class Meta:
        verbose_name = '密码重置Token'
        verbose_name_plural = '密码重置Token'

    # 用户学号
    student = models.ForeignKey(to=StuInfo, on_delete=models.CASCADE, blank=True, null=True, verbose_name='关联学生')

    # 用户工号
    teacher = models.ForeignKey(to=TecInfo, on_delete=models.CASCADE, blank=True, null=True, verbose_name='关联教师')

    # 临时Token
    token = models.CharField(max_length=64, blank=False, verbose_name='临时Token')

    def __str__(self):
        return self.token
