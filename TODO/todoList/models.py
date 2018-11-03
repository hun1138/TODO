from django.db import models

# Create your models here.
class Todo(models.Model):
    todo_title = models.CharField(max_length=20)
    todo_detail = models.TextField(null=True)
    todo_due_date = models.DateTimeField(null=True)
    todo_is_complete = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)