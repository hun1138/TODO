from django import forms
from .models import Todo


class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ['todo_title', 'todo_detail']
'''
class TodoForm(forms.Form):
    todo_title = forms.CharField(label='title', max_length=20)
    todo_info = forms.CharField(label='info', widget=forms.Textarea)
    #todo_due_date = forms.DateTimeField(widget=forms.DateInput)
    todo_due_date = forms.DateField(widget=forms.SelectDateWidget)
'''