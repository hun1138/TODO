from django.contrib import admin

from .models import Todo

# Register your models here.

class TodoAdmin(admin.ModelAdmin):
    field = ['todo_title', 'todo_info']

admin.site.register(Todo, TodoAdmin)