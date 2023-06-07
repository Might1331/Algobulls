from django.contrib import admin
from todo.models import Task
# Register your models here.

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['__str__','id','Title','Timestamp', 'Status','Due_date','Tags','Description']
    
    # def Tags(self,obj):
    #     tags=set(obj.Tags.split(','))
    #     tags=list(tags)
    #     return tags