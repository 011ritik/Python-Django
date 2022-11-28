from django.shortcuts import render
from .models import Room
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def roomview(request):
    rooms = Room.objects.all()
    return render(request, 'rooms.html', context={'rooms':rooms})

def room_detail(request, slug):
    room = Room.objects.get(slug=slug)
    return render(request, 'room_detail.html', context={'room':room})