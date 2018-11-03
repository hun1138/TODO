from django.shortcuts import render, get_object_or_404
from django.views import generic

import datetime

from .models import Todo
from .forms import TodoForm

# Create your views here.
def index(request):
    if request.method == 'POST':
        todoForm = TodoForm(request.POST)
        #print(todoForm)
        print(todoForm.data['todo_due_date'])
        if todoForm.is_valid():
            todoForm.save()
    else:
        todoForm = TodoForm()

    todoList = Todo.objects.all()
    todoLen = len(todoList)
    context = {
        'todoForm':todoForm,
        'todoList':todoList,
        'todoLen':todoLen,
    }
    return render(request, 'todo/index.html', context)

class DetailView(generic.DetailView):
    model = Todo
    template_name = 'todo/detail.html'