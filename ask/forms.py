from django import forms

from .models import Question, Answer


class QuesForm(forms.ModelForm):

    class Meta:
        model = Question
        fields = ('title', 'optional_description',)

class AnswerForm(forms.ModelForm):

    class Meta:
        model = Answer
        fields = ('author', 'text',)
