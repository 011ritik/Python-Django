from .views import TodoIndex, todoList
from django.urls import path

urlpatterns = [
    path('', TodoIndex.as_view(), name="index")
]