from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone

from .models import Question

# Create your views here.


def home(request):
    return render(request, 'ask/home.html')

def about(request):
    return render(request, 'ask/about.html')

def ques_list(request):
    ques = Question.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'ask/ques_list.html', {'ques': ques})
