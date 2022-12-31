from django.shortcuts import render
from django.urls import reverse_lazy
from .forms import NoteFormView
from .models import Notes
from django.views.generic import ListView, DetailView,CreateView, DeleteView, UpdateView

# Create your views here.

class IndexView(ListView):
    template_name = 'index.html'
    model = Notes
    fields = ['title', 'des']

    def get_queryset(self):
        return Notes.objects.all()
    
    def des(self, model):
        return Notes.description[:100]

class NoteDetailView(DetailView):
    template_name = 'note_detail.html'
    model = Notes

class NoteCreateView(CreateView):
    form_class = NoteFormView
    template_name = 'create_note.html'
    success_url = reverse_lazy('index')

class DeleteNoteView(DeleteView):
    model = Notes
    success_url = reverse_lazy('index')
    template_name = 'delete.html'

class UpdateNoteView(UpdateView):
    model = Notes
    fields = ['title', 'description']
    success_url = reverse_lazy('index')
    template_name = 'edit_note.html'
    
