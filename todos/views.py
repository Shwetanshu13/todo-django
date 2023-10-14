from django.shortcuts import render
from todos.models import TodoList
# Create your views here.

def home(request):
    return render(request,"home.html")

def todos(request):
    if request.method == "POST":
        newTodo = request.POST.get('newtodo')
        print(newTodo)
        addTodo = TodoList(todoStatus=False, todoName=newTodo)
        addTodo.save()
    todos = TodoList.objects.all()
    params = {'todoList':todos}
    return render(request, "todos.html", params)

def addTodo(request):
    return render(request, 'addTodo.html')

def delTodo(request):
    return render(request, 'delTodo.html')
