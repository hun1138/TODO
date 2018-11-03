from django.shortcuts import render, get_object_or_404
from django.views import generic

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
        print(todoForm.as_p())
    todoList = Todo.objects.all()
    todoLen = len(todoList)
    context = {
        #'todoForm':todoForm,
        'todoList':todoList,
        'todoLen':todoLen,
    }
    return render(request, 'todo/index.html', context)

class DetailView(generic.DetailView):
    model = Todo
    template_name = 'todo/detail.html'