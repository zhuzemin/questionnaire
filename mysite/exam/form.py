from django import forms

class examForm(forms.Form):
    interviewee = forms.CharField()
    genre = forms.IntegerField()
    quizNum = forms.IntegerField()
    duration = forms.IntegerField()


class quizForm(forms.Form):
    name = forms.CharField()
    option = forms.IntegerField()
    quizNum = forms.IntegerField()
    duration = forms.IntegerField()
