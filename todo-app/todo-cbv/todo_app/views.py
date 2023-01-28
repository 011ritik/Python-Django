from django.shortcuts import render
from django.views.generic import ListView, CreateView, DeleteView, UpdateView
from .models import TodoModel
# Create your views here.

class TodoIndex(ListView):
    template_name = "todo_app/todolistview.html"
    model = TodoModel 
    # context_object_name = 'todo_list'
    # default context_object_name is todomodel_list (model name in all lowercase )

def todoList(request):
    if request.method == 'GET':
        model = TodoModel
        todo_list = model.objects.all()
        return render(request, 'todo_app/todolistview.html', {'todo_list': todo_list})
    
    return '<h1>Error </h1>'