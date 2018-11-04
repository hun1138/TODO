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
        if todoForm.is_valid():
            todoForm.save()
    else:
        todoForm = TodoForm()

    todoList = Todo.objects.filter(todo_is_complete=False)
    todoCompleteList = Todo.objects.filter(todo_is_complete=True)
    todoListLen = len(todoList)
    todoCompleteListLen = len(todoCompleteList)
    todayDate = datetime.datetime.now().strftime('%Y-%m-%d')
    context = {
        'todoForm':todoForm,
        'todoList':todoList,
        'todoCompleteList': todoCompleteList,
        'todoListLen':todoListLen,
        'todoCompleteListLen': todoCompleteListLen,
        'todayDate': todayDate,
    }
    return render(request, 'todo/index.html', context)

def delete(request, todo_id):
    todo = get_object_or_404(Todo, id=todo_id)
    todo.delete()
    return HttpResponseRedirect(reverse('todoList:index'))

def complete(request, todo_id):
    todo = get_object_or_404(Todo, id=todo_id)
    todo.todo_is_complete = True
    todo.save()
    return HttpResponseRedirect(reverse('todoList:index'))

def cancel(request, todo_id):
    todo = get_object_or_404(Todo, id=todo_id)
    todo.todo_is_complete = False
    todo.save()
    return HttpResponseRedirect(reverse('todoList:index'))

def update(request, todo_id):
    if request.method == 'POST':
        todo = get_object_or_404(Todo, id=todo_id)
        todoForm = TodoForm(request.POST or None, instance=todo)

        if todoForm.is_valid():
            todoForm.save()
    return HttpResponseRedirect(reverse('todoList:index'))

class DetailView(generic.DetailView):
    model = Todo
    template_name = 'todo/detail.html'