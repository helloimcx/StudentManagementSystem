from django.contrib import admin
from MainApp.models import QuestionInfo, RoleInfo, RolePurview, TeacherRole,\
    PurviewInfo, PasswordResetToken, TeacherPurview, StuInfo, TecInfo


# Register your models here.
admin.site.register(TeacherPurview)
admin.site.register(TeacherRole)
admin.site.register(PurviewInfo)
admin.site.register(RolePurview)
admin.site.register(PasswordResetToken)
admin.site.register(StuInfo)
admin.site.register(QuestionInfo)
admin.site.register(RoleInfo)
admin.site.register(TecInfo)
