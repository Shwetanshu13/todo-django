from django.shortcuts import render

# Create your views here.

def todos(request):
    return render(request, "todos.html")

def addTodo(request):
    return render(request, 'todos.html')

def delTodo(request):
    return render(request, 'todos.html')
