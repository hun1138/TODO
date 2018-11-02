from django.urls import path

from . import views

app_name = 'todoList'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:todo_id>/detail/', views.detail, name='detail'),
]