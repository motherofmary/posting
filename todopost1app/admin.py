from django.contrib import admin
from django.contrib import admin
from . models import Task
# Register your models here.

class TaskAdmin(admin.ModelAdmin):
    list_display = ['title', 'desc', 'date']
    list_editable = ['desc', 'date']

admin.site.register(Task,TaskAdmin)
