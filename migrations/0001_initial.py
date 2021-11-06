# Generated by Django 3.0.5 on 2020-04-18 07:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PurviewInfo',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False, verbose_name='编号')),
                ('pid', models.IntegerField(blank=True, verbose_name='上级权限编号')),
                ('purviewName', models.CharField(max_length=45, verbose_name='权限名称')),
                ('purviewUrl', models.URLField(blank=True, verbose_name='权限请求')),
            ],
            options={
                'verbose_name': '权限信息',
                'verbose_name_plural': '权限信息',
            },
        ),
        migrations.CreateModel(
            name='QuestionInfo',
            fields=[
                ('questionNo', models.IntegerField(primary_key=True, serialize=False, verbose_name='密保问题编号')),
                ('question', models.CharField(max_length=30, verbose_name='密保问题')),
            ],
            options={
                'verbose_name': '密保问题',
                'verbose_name_plural': '密保问题',
            },
        ),
        migrations.CreateModel(
            name='RoleInfo',
            fields=[
                ('roleNo', models.IntegerField(primary_key=True, serialize=False, verbose_name='角色编号')),
                ('roleName', models.CharField(max_length=45, verbose_name='角色名称')),
                ('createTime', models.DateField(verbose_name='创建日期')),
                ('roleDescription', models.TextField(blank=True, verbose_name='角色描述')),
            ],
            options={
                'verbose_name': '角色信息',
                'verbose_name_plural': '角色信息',
            },
        ),
        migrations.CreateModel(
            name='TecInfo',
            fields=[
                ('teacherNo', models.CharField(max_length=4, primary_key=True, serialize=False, verbose_name='工号')),
                ('password', models.CharField(max_length=12, verbose_name='密码')),
                ('answer', models.CharField(blank=True, max_length=30, verbose_name='密保问题答案')),
                ('tecStatus', models.BooleanField(default=True, verbose_name='在职状态')),
                ('email', models.CharField(blank=True, max_length=128, verbose_name='邮箱')),
                ('questionNo', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='MainApp.QuestionInfo', verbose_name='密保问题编号')),
            ],
            options={
                'verbose_name': '教师信息',
                'verbose_name_plural': '教师信息',
            },
        ),
        migrations.CreateModel(
            name='TeacherRole',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('roleNo', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='MainApp.RoleInfo', verbose_name='角色编号')),
                ('teacherNo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MainApp.TecInfo', verbose_name='教师编号')),
            ],
            options={
                'verbose_name': '教师角色关联',
                'verbose_name_plural': '教师角色关联',
            },
        ),
        migrations.CreateModel(
            name='TeacherPurview',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('purviewNo', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='MainApp.PurviewInfo', verbose_name='权限编号')),
                ('teacherNo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MainApp.TecInfo', verbose_name='教师编号')),
            ],
            options={
                'verbose_name': '教师权限关联',
                'verbose_name_plural': '教师权限关联',
            },
        ),
        migrations.CreateModel(
            name='StuInfo',
            fields=[
                ('studentNo', models.CharField(max_length=8, primary_key=True, serialize=False, verbose_name='学号')),
                ('password', models.CharField(max_length=12, verbose_name='密码')),
                ('answer', models.CharField(blank=True, max_length=30, verbose_name='密保问题答案')),
                ('stuStatus', models.BooleanField(default=True, verbose_name='状态，是否为该校学生')),
                ('email', models.CharField(blank=True, max_length=128, verbose_name='邮箱')),
                ('questionNo', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='MainApp.QuestionInfo', verbose_name='密保问题')),
            ],
            options={
                'verbose_name': '学生信息',
                'verbose_name_plural': '学生信息',
            },
        ),
        migrations.CreateModel(
            name='RolePurview',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('purviewNo', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='MainApp.PurviewInfo', verbose_name='权限编号')),
                ('roleNo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MainApp.RoleInfo', verbose_name='角色编号')),
            ],
            options={
                'verbose_name': '角色权限关联',
                'verbose_name_plural': '角色权限关联',
            },
        ),
        migrations.CreateModel(
            name='PasswordResetToken',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('token', models.CharField(max_length=64, verbose_name='临时Token')),
                ('student', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='MainApp.StuInfo', verbose_name='关联学生')),
                ('teacher', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='MainApp.TecInfo', verbose_name='关联教师')),
            ],
            options={
                'verbose_name': '密码重置Token',
                'verbose_name_plural': '密码重置Token',
            },
        ),
    ]