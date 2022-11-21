from django.shortcuts import render, get_object_or_404
from .models import Question
from django.views.generic import ListView, DetailView
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.
class Index(ListView):
    template_name = 'index.html'
    context_object_name = 'question_list'

    def get_queryset(self):
        return Question.objects.order_by('pub_date')[:5]

class Detail(DetailView):
    model = Question
    template_name = 'detail.html'


def choices(request, pk):
    res = get_object_or_404(Question, pk=pk)
    try:
        selected = res.choices_set.get(pk=request.POST['choice'])
    except(KeyError):
        return render(request,'detail.html',{
            'res': res,
            'error_message': "You didn't select a choice.",
        })

    else:
        selected.vote += 1
        selected.save()
        return HttpResponseRedirect(reverse('polls:result',args=(res.pk,)))

class Result(DetailView):
    model = Question
    template_name = 'result.html'