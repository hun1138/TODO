from django import forms
from .models import Todo

import datetime

class TodoForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(TodoForm, self).__init__(*args, **kwargs)
        self.fields['todo_detail'].required = False
        self.fields['todo_due_date'].required = False

    class Meta:
        model = Todo
        fields = ['todo_title', 'todo_detail', 'todo_due_date']

        todayDate = datetime.datetime.now().strftime('%Y-%m-%d')

        labels = {
            'todo_title': '제목',
            'todo_detail': '내용',
            'todo_due_date': '마감기한',
        }
        widgets = {
            'todo_title': forms.TextInput(attrs={'class': 'form-control'}),
            'todo_detail': forms.Textarea(attrs={'class': 'form-control', 'rows': 10}),
            'todo_due_date': forms.DateInput(attrs={'type':'date', 'class': 'form-control', 'min': todayDate}),
        }
        error_messages = {
            'todo_title': {
                'required': '제목을 입력해주세요',
            },
            'todo_due_date': {
                'required': '형식이 맞지 않습니다',
            },
        }