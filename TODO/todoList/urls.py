from django.urls import path

from . import views

app_name = 'todoList'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:todo_id>/delete/', views.delete, name='delete'),
    path('<int:todo_id>/complete/', views.complete, name='complete'),
    path('<int:todo_id>/cancel/', views.cancel, name='cancel'),
    path('<int:pk>/detail/', views.DetailView.as_view(), name='detail'),
]