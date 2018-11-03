from django.urls import path

from . import views

app_name = 'todoList'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:pk>/detail/', views.DetailView.as_view(), name='detail'),
]