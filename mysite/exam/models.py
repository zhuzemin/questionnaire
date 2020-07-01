from django.db import models
# Create your models here.
from django.utils.timezone import now


class answer(models.Model):
    name = models.CharField(max_length=30)
    correct = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class type(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class genre(models.Model):
    name = models.CharField(max_length=20, default='unknown')

    def __str__(self):
        return self.name


class quiz(models.Model):
    type = models.ForeignKey(type, on_delete=models.PROTECT)
    genre = models.ForeignKey(genre, on_delete=models.PROTECT)
    name = models.CharField(max_length=3000)
    option = models.ManyToManyField(answer, related_name="option")
    #answer = models.ManyToManyField(answer)
    #description = models.CharField(max_length=3000)

    def __str__(self):
        return self.name


class interviewee(models.Model):
    name = models.CharField(max_length=10)

    def __str__(self):
        return self.name


class exam(models.Model):
    uuid = models.UUIDField()
    quiz = models.ManyToManyField(quiz)
    userAnswer = models.CharField(max_length=1024, null=True, blank=True)
    logtime = models.DateTimeField(default=now)
    interviewee = models.CharField(max_length=10)
    status = models.IntegerField(default=0)
    startTime = models.DateTimeField(null=True, blank=True)
    endTime = models.DateTimeField(null=True, blank=True)
    duration = models.IntegerField(default=10)
    allowIP = models.GenericIPAddressField(null=True, blank=True)
    quizNum = models.IntegerField(default=10)

    def __unicode__(self):
        return self.uuid

