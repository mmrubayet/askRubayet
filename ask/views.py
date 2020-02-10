from django.http import HttpResponse
from django.utils import timezone
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required

from .models import Question
from .forms import QuesForm, AnswerForm
# Create your views here.


def home(request):
    return render(request, 'ask/home.html')

def about(request):
    return render(request, 'ask/about.html')

def ques_list(request):
    ques = Question.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, 'ask/ques_list.html', {'ques': ques})

def ques_detail(request, pk):
    que = get_object_or_404(Question, pk=pk)
    return render(request, 'ask/ques_detail.html', {'que': que})

def ques_publish(request, pk):
    que = get_object_or_404(Question, pk=pk)
    que.publish()
    return redirect('ques_detail', pk=pk)

@login_required
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

@login_required
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

@login_required
def ques_draft_list(request):
    ques = Question.objects.filter(published_date__isnull=True).order_by('created_date')
    return render(request, 'ask/ques_draft_list.html', {'ques': ques})

@login_required
def ques_remove(request, pk):
    que = get_object_or_404(Question, pk=pk)
    que.delete()
    return redirect('ques_draft_list')

def add_answer_to_que(request, pk):
    que = get_object_or_404(Question, pk=pk)
    if request.method == 'POST':
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.que = que
            # answer.que.author = request.user
            answer.save()
            return redirect('ques_detail', pk=que.pk)
    else:
        form = AnswerForm()
    return render(request, 'ask/add_answer_to_que.html', {'form': form})
