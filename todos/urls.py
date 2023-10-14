from django.urls import path
from . import views

urlpatterns = [
    path('todos/', views.todos, name="todos"),
    path('addTodo/', views.addTodo, name="addTodo"),
    path('delTodo', views.delTodo, name="delTodo"),
    
]
