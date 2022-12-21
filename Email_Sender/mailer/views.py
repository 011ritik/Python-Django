from django.shortcuts import render
from .forms import EmailSender
from django.core.mail import send_mail

# Create your views here.
def index(request):
    mailSend = False
    if request.method == "POST":
        form = EmailSender(request.POST)

        if form.is_valid():
            userIn = form.cleaned_data
            to = userIn['to']
            subject = userIn['subject']
            message = userIn['message']
            
            send_mail(subject, message, 'mymail@gmail.com', [to])
            mailSend = True

        else:
            form = EmailSender

        return render(request, 'index.html', {'form': form , 'mailSend':mailSend })
    
    else:
        form = EmailSender()
        return render(request, 'index.html', {'form': form})
