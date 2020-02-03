from django import forms

from .models import Question


class QuesForm(forms.ModelForm):

    class Meta:
        model = Question
        fields = ('title', 'optional_description',)
