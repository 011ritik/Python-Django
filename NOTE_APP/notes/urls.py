from django.urls import path
from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name="index"),
    path('add/', views.NoteCreateView.as_view(), name='add_note'),
    path('note-detail/<int:pk>/', views.NoteDetailView.as_view(), name='note_detail'),
    path('note-delete/<int:pk>/', views.DeleteNoteView.as_view(), name='delete'),
    path('note-edit/<int:pk>/', views.UpdateNoteView.as_view(), name='update'),
]