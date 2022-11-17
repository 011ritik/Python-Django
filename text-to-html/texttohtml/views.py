from django.shortcuts import render
from .models import Parser
from .forms import ParserForm

# Create your views here.
def index(request):
    return render(request, 'index.html')

def converter(request):
    form = ParserForm
    return render(request, 'converter.html', {'form':form})