from django.contrib import admin
from tasks.models import Task, Sub_Task
# Register your models here.

admin.site.register(Task)
admin.site.register(Sub_Task)