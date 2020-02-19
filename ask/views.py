from django.http import HttpResponse
from django.utils import timezone
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.views.generic import (TemplateView, ListView, DetailView,
                                    CreateView, UpdateView, DeleteView,
                                     )
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from .models import Question, Answer
from .forms import QuesForm, AnswerForm
# Create your views here.


def home(request):
    return render(request, 'ask/home.html')

def about(request):
    return render(request, 'ask/about.html')

def question_list(request):
    ques = Question.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, 'ask/question_list.html', {'ques': ques})

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
def question_draft_list(request):
    ques = Question.objects.filter(published_date__isnull=True).order_by('created_date')
    return render(request, 'ask/question_draft_list.html', {'ques': ques})

# class QuestionDraftListView(LoginRequiredMixin, ListView):
#     login_url = '/login/'
#     redirect_field_name = 'ask/question_list.html'
#     model = Question
#
#     def get_queryset(self):
#         return Question.objects.filter(published_date__isnull=True).order_by('created_date')


class UserQuestionListView(ListView):
    model = Question
    template_name = 'ask/user_question_list.html'
    context_object_name = 'questions'
    # paginate_by = 4

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Question.objects.filter(author=user).order_by('-created_date')


# @login_required
# def ques_remove(request, pk):
#     que = get_object_or_404(Question, pk=pk)
#     que.delete()
#     return redirect('ques_draft_list')

class QuestionDeleteView(LoginRequiredMixin, DeleteView):
    model =  Question
    success_url = reverse_lazy('question_list')

@login_required
def answer_approve(request, pk):
    answer = get_object_or_404(Answer, pk=pk)
    answer.approve()
    return redirect('ques_detail', pk=answer.question.pk)

# @login_required
# def answer_remove(request, pk):
#     answer = get_object_or_404(Answer, pk=pk)
#     answer.delete()
#     return redirect('ques_detail', pk=answer.question.pk)

class AnswerDeleteView(LoginRequiredMixin, DeleteView):
    model =  Answer
    success_url = reverse_lazy('question_list')

@login_required
def answer_hide(request, pk):
    answer = get_object_or_404(Answer, pk=pk)
    answer.hide()
    return redirect('ques_detail', pk=answer.question.pk)



def add_answer_to_que(request, pk):
    que = get_object_or_404(Question, pk=pk)
    if request.method == 'POST':
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.question = que
            answer.save()
            return redirect('ques_detail', pk=que.pk)
    else:
        form = AnswerForm()
    return render(request, 'ask/add_answer_to_que.html', {'form': form})
