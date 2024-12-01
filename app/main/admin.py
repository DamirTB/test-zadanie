from django.contrib import admin
from .models import Task

# Register your models here.


class TaskAdmin(admin.ModelAdmin):
    list_display = ('name', 'priority', 'status', 
                    'finished', 'created', )
    list_filter = ('priority', 'status', )


admin.site.register(Task, TaskAdmin)
