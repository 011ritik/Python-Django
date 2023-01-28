from django.urls import path
from . import views

urlpatterns = [
    path('', views.indexList, name="index"),
    path('update/<int:pk>', views.updateTask, name="update"),
    path('create/', views.createTask, name="create"),
    path('delete/<int:id>', views.deleteTask, name="delete"),


]