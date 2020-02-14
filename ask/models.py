from django.conf import settings
from django.db import models
from django.utils import timezone


class Question(models.Model):
    author                  = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title                   = models.CharField(max_length=300)
    optional_description    = models.TextField(blank=True, null=True)
    created_date            = models.DateTimeField(default=timezone.now)
    published_date          = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def approved_answer(self):
        return self.answer.filter(approved_answer=True)

    def __str__(self):
        return self.title


class Answer(models.Model):
    question            = models.ForeignKey('ask.question', on_delete=models.CASCADE, related_name='answer')
    author              = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    text                = models.TextField()
    created_date        = models.DateTimeField(default=timezone.now)
    approved_answer     = models.BooleanField(default=False)


    def approve(self):
        self.approved_answer = True
        self.save()

    def hide(self):
        self.approved_answer = False
        self.save()


    def __str__(self):
        return self.text
