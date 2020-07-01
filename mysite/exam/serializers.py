from rest_framework import serializers
from mysite.exam.models import *


class answerSerializer(serializers.Serializer):
    name = serializers.CharField()
    correct = serializers.BooleanField()

    class Meta:
        model = answer
        fields = '__all__'


class quizSerializer(serializers.Serializer):
    type = serializers.CharField()
    genre = serializers.CharField()
    name = serializers.CharField()
    option = answerSerializer(many=True)
    #answer = answerSerializer(many=True)

    class Meta:
        model = quiz
        fields = '__all__'


class examSerializer(serializers.Serializer):
    quiz = quizSerializer(many=True)
    interviewee = serializers.CharField()
    uuid = serializers.UUIDField()
    userAnswer = serializers.CharField()
    logtime = serializers.DateTimeField()
    status = serializers.IntegerField()
    startTime = serializers.DateTimeField()
    endTime = serializers.DateTimeField()
    duration = serializers.IntegerField()
    allowIP = serializers.IPAddressField()
    quizNum = serializers.IntegerField()

    class Meta:
        model = exam
        fields = '__all__'
