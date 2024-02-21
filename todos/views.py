from django.shortcuts import render, HttpResponseRedirect
from todos.models import TodoList
# Create your views here.

def home(request):
    return render(request,"home.html")

def todos(request):
    if request.method == "POST":
        delTodo = request.POST.get('deltodo')
        print(delTodo, "deleted")
    todos = TodoList.objects.all()
    params = {'todoList':todos}
    return render(request, "todos.html", params)

def addTodo(request):
    if request.method == "POST":
        newTodo = request.POST.get('newtodo')
        print(newTodo)
        addTodo = TodoList(todoStatus=False, todoName=newTodo)
        addTodo.save()
        return HttpResponseRedirect("/todos")
    return render(request, 'addTodo.html')

def delTodo(request):
    if request.method == "POST":
        delTodo = request.POST.get('deltodo')
        print(delTodo, "deleted")
        return HttpResponseRedirect("/todos")
    todos = TodoList.objects.all()
    params = {'todoList':todos}
    return render(request, 'delTodo.html', params)

