from django.shortcuts import render, get_object_or_404

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
    todoList = Todo.objects.all()
    todoLen = len(todoList)
    context = {
        'todoForm':todoForm,
        'todoList':todoList,
        'todoLen':todoLen,
    }
    return render(request, 'index.html', context)

def detail(request, todo_id):
    todo = get_object_or_404(Todo, pk=todo_id)
    context = {
        'todo':todo,
    }
    return render(request, 'detail.html', context)