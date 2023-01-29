from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.TodoCreateView.as_view(), name="create"),
    path('', views.TodoListView.as_view(), name="index"),
    path('delete/<int:pk>/', views.TodoDeleteView.as_view(), name="delete"),
    path('update/<int:pk>/', views.TodoUpdateView.as_view(), name="update"),
]