from django.contrib import admin

# Register your models here.
from Django3App import models

admin.site.register(models.Student)
admin.site.register(models.Parent)
admin.site.register(models.LoginView)
admin.site.register(models.Attendance)
admin.site.register(models.AlotRoom)