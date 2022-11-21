from django.urls import path
from . import views

app_name = 'polls'

urlpatterns = [
    path('index/', views.Index.as_view(), name="index"),
    path('question/<int:pk>/', views.Detail.as_view(), name="detail"),
    path('question/<int:pk>/result/', views.Result.as_view(), name="result"),
    path('question/<int:pk>/choices/', views.choices, name='choice')
]