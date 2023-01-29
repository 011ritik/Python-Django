from django.shortcuts import render
from django.views.generic import ListView, DeleteView, FormView, UpdateView, CreateView
from .models import TodoModel
from .forms import TodoForm

# Create your views here.
class TodoListView(ListView):
    model = TodoModel
    # queryset = TodoModel.objects.all()
    context_object_name = "todo_list"
    template_name = 'todo_app/index.html'


class TodoDeleteView(DeleteView):
    model = TodoModel
    template_name = "todo_app/tododelete.html"
    success_url = "/"

class TodoCreateView(CreateView):
    model = TodoModel
    fields = "__all__"
    template_name = "todo_app/todocreate.html"
    success_url = "/"

class TodoUpdateView(UpdateView):
    model = TodoModel
    fields = '__all__'
    template_name = "todo_app/todoupdate.html"
    success_url = "/"