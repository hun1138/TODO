from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.http import HttpResponseRedirect
from django.urls import reverse

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

    todoList = Todo.objects.filter(todo_is_complete=False)
    todoCompleteList = Todo.objects.filter(todo_is_complete=True)
    todoListLen = len(todoList)
    todoCompleteListLen = len(todoCompleteList)
    context = {
        'todoForm':todoForm,
        'todoList':todoList,
        'todoCompleteList': todoCompleteList,
        'todoListLen':todoListLen,
        'todoCompleteListLen': todoCompleteListLen,
    }
    return render(request, 'todo/index.html', context)

def delete(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    todo.delete()
    return HttpResponseRedirect(reverse('todoList:index'))

def complete(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    todo.todo_is_complete = True
    todo.save()
    return HttpResponseRedirect(reverse('todoList:index'))

def cancel(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    todo.todo_is_complete = False
    todo.save()
    return HttpResponseRedirect(reverse('todoList:index'))

def update(request, todo_id):
    if request.method == 'POST':
        todo = Todo.objects.get(id=todo_id)
        todo.todo_title = request.POST['todo_title']
        todo.todo_detail = request.POST['todo_detail']
        if request.POST['todo_due_date'] == '':
            todo.todo_due_date = None
        todo.save()
    return HttpResponseRedirect(reverse('todoList:index'))

class DetailView(generic.DetailView):
    model = Todo
    template_name = 'todo/detail.html'