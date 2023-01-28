from django.shortcuts import render, redirect
from .models import TodoModel
from .forms import TodoForm

# Create your views here.
def index(request):
    return render(request, 'base.html')

def indexList(request):
    model = TodoModel
    tasks_list = model.objects.all()
    return render(request, 'todo_app/index.html', {'tasks_list':tasks_list})

def createTask(request):
    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()

        return redirect('index')
    form = TodoForm()
    return render(request, 'todo_app/create.html', {'form': form})

def updateTask(request, pk):

    model = TodoModel
    obj = model.objects.get(id=pk)
    form = TodoForm(instance=obj)

    if request.method == "POST":
        form = TodoForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
        return redirect('index')

    return render(request, 'todo_app/update.html', {'form': form})

    
def deleteTask(request, id):
    model = TodoModel
    obj = model.objects.get(id = id)

    if request.method == "POST":
        obj.delete()

        return redirect('index')
    return render(request, 'todo_app/delete.html' ,{'task':obj})
        