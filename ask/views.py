from django.http import HttpResponse
from django.utils import timezone
from django.shortcuts import render, get_object_or_404, redirect

from .models import Question
from .forms import QuesForm
# Create your views here.


def home(request):
    return render(request, 'ask/home.html')

def about(request):
    return render(request, 'ask/about.html')

def ques_list(request):
    ques = Question.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, 'ask/ques_list.html', {'ques': ques})

def ques_draft_list(request):
    ques = Question.objects.filter(published_date__isnull=True).order_by('created_date')
    return render(request, 'ask/ques_draft_list.html', {'ques': ques})

def ques_detail(request, pk):
    que = get_object_or_404(Question, pk=pk)
    return render(request, 'ask/ques_detail.html', {'que': que})

def ques_publish(request, pk):
    que = get_object_or_404(Question, pk=pk)
    que.publish()
    return redirect('ques_detail', pk=pk)

def ques_unpublish(request, pk):
    que = get_object_or_404(Question, pk=pk)
    que.unpublish()
    return redirect('ques_detail', pk=pk)

def ques_new(request):
    if request.method == 'POST':
        form = QuesForm(request.POST)
        if form.is_valid():
            que = form.save(commit=False)
            que.author = request.user
            que.save()
            return redirect('ques_detail', pk=que.pk)
    else:
        form = QuesForm()

    return render(request, 'ask/ques_edit.html', {'form': form})

def ques_edit(request, pk):
    que = get_object_or_404(Question, pk=pk)
    if request.method == 'POST':
        form = QuesForm(request.POST, instance=que)
        if form.is_valid():
            que = form.save(commit=False)
            que.author = request.user
            que.save()
            return redirect('ques_detail', pk=que.pk)
    else:
        form = QuesForm(instance=que)

    return render(request, 'ask/ques_edit.html', {'form': form})
