
import datetime

from django.db import models
from django.utils import timezone

# Create your models here.
class Woeids(models.Model):
    country = models.CharField(max_length=200, null=True, blank=True)
    name = models.CharField(max_length=200, null=True, blank=True)
    woeid = models.IntegerField(default=0, null=True, blank=True)

    def __str__(self):
        return '%s %s %s' % (
        self.country,
        self.name,
        str(self.woeid)
        )

# From tutorial: https://docs.djangoproject.com/en/3.0/intro/tutorial02/
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
