from django.contrib import admin

# Register your models here.
from StudentMessage.models import StuBasicInfo, ClassInfo, MajorInfo, DepInfo

admin.site.register(StuBasicInfo)
admin.site.register(DepInfo)
admin.site.register(MajorInfo)
admin.site.register(ClassInfo)