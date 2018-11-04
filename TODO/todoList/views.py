from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.http import HttpResponseRedirect
from django.urls import reverse

from datetime import datetime, timedelta

from .models import Todo
from .forms import TodoForm

from django.db.models import Q

# Create your views here.
def index(request):
    if request.method == 'POST':
        todoForm = TodoForm(request.POST)
        if todoForm.is_valid():
            todoForm.save()
    else:
        todoForm = TodoForm()

    todayDate = datetime.now().strftime('%Y-%m-%d')
    todayDate_m = datetime.today() - timedelta(days=1)
    todayDate_m = todayDate_m.strftime('%Y-%m-%d')

    todoList = Todo.objects.filter(Q(todo_due_date__range=[todayDate, '5000-12-31']) | Q(todo_due_date=None), todo_is_complete=False)
    todoListLen = len(todoList)

    todoCompleteList = Todo.objects.filter(todo_is_complete=True)
    todoCompleteListLen = len(todoCompleteList)

    todoPassedList = Todo.objects.filter(todo_is_complete=False, todo_due_date__range=['1000-01-01', todayDate_m])
    todoPassedListLen = len(todoPassedList)
    context = {
        'todoForm':todoForm,
        'todayDate': todayDate,
        'todoList':todoList,
        'todoListLen': todoListLen,
        'todoCompleteList': todoCompleteList,
        'todoCompleteListLen': todoCompleteListLen,
        'todoPassedList': todoPassedList,
        'todoPassedListLen': todoPassedListLen,
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