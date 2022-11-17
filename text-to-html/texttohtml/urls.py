from django.urls import path
from . import views

app_name='texttohtml'

urlpatterns = [
    path('',views.index, name='index'),
    path('converter/', views.converter, name='converter')
]