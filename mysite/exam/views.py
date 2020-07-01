import random as rand
from django.db.models import Max
from django.shortcuts import render
import re
from mysite.exam.models import genre, type, exam, quiz, answer
from django.utils.timezone import now
from mysite.exam.serializers import examSerializer
from django.http import JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from mysite.exam.form import examForm, quizForm
import uuid
import datetime


def examView(request):
    errors = []
    if 'uuid' in request.GET:
        uuid = request.GET['uuid']
        if not uuid:
            errors.append('uuid is blank.')
        elif not re.match(r"\w{8}-{1,4}\w{4}-{1,4}\w{4}-{1,4}\w{4}-{1,4}\w{12}", uuid):
            errors.append('uuid is invalid.')
        else:
            _exam = exam.objects.get(uuid=uuid)
            if not _exam.allowIP:
                _exam.allowIP = request.META['REMOTE_ADDR']
                _exam.save()
                return render(request, 'exam.html', {'exam': _exam})
            elif _exam.allowIP == request.META['REMOTE_ADDR'] or _exam.status == 2:
                return render(request, 'exam.html', {'exam': _exam})
            else:
                return HttpResponse('500 Internal Server Error')
    return render(request, 'invalid url.', )


def exam_info(request):
    response = {}
    data = {}
    errors = []
    if 'uuid' in request.GET:
        _uuid = request.GET['uuid']
        if not _uuid:
            errors.append('uuid is blank.')
        elif not re.match(r"\w{8}-{1,4}\w{4}-{1,4}\w{4}-{1,4}\w{4}-{1,4}\w{12}", _uuid):
            errors.append('uuid is invalid.')
        else:
            _exam = exam.objects.get(uuid=_uuid)
            if _exam.status == 0:
                _exam.status = 1
                _exam.startTime = now()
                _exam.endTime = _exam.startTime+datetime.timedelta(minutes=_exam.duration)
                _exam.save()
            data = examSerializer(_exam).data
    if errors:
        response['error'] = True
        response['body'] = errors
    else:
        response['error'] = False
        response['body'] = data
    return JsonResponse(response)


@csrf_exempt
def post_answer(request):
    response = {}
    errors = []
    data = {}
    _json = json.loads(request.body.decode('utf-8'))
    _uuid = _json['uuid']
    if not _uuid:
        errors.append('uuid is blank.')
    elif not re.match(r"\w{8}-{1,4}\w{4}-{1,4}\w{4}-{1,4}\w{4}-{1,4}\w{12}", _uuid):
        errors.append('uuid is invalid.')
    else:
        _exam = exam.objects.get(uuid=_uuid)
        if _exam.status == 1:
            _exam.status = 2
            for JSONquiz in _json['quiz']:
                for MODELquiz in _exam.quiz.all():
                    if JSONquiz['name'] == MODELquiz.name:
                        for MODELanswer in MODELquiz.answer.all():
                            for JSONanswer in JSONquiz['answer']:
                                if JSONanswer == MODELanswer.name:
                                    JSONquiz['correct'] = True
                                    break
                                elif JSONanswer == JSONquiz['answer'][-1]:
                                    JSONquiz['correct'] = False
            _exam.userAnswer = json.dumps(_json['quiz'])
            _exam.save()
        data = examSerializer(_exam).data
    if errors:
        response['error'] = True
        response['body'] = errors
    else:
        response['error'] = False
        response['body'] = data
    return JsonResponse(response)


@csrf_exempt
def generate(request):
    response = {}
    if request.method == 'POST':
        form = examForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            _uuid = uuid.uuid1()
            quizNum=cd['quizNum']
            _exam = exam.objects.create(
                uuid=_uuid,
                interviewee=cd['interviewee'],
                quizNum=quizNum,
                duration=cd['duration'],
            )
            for n in [1, quizNum]:
                _quiz = get_random(quiz, cd['genre'])
                _exam.quiz.add(_quiz)
            _exam.save()
            data = {'uuid': _uuid}
            response['error'] = False
            response['body'] = data
        else:
            response['error'] = True
            response['body'] = form.errors
        return JsonResponse(response)
    else:
        genres = genre.objects.all()
        return render(request, 'generate.html', {"genres": genres})


def get_random(model, genreId):
    _genre = genre.objects.get(id=genreId)
    max_id = model.objects.filter(genre=_genre).aggregate(max_id=Max("id"))['max_id']
    while True:
        pk = rand.randint(1, max_id)
        object = model.objects.filter(pk=pk).first()
        if object:
            return object


@csrf_exempt
def importView(request):
    response = {}
    if request.method == 'POST':
        form = examForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            _quiz = quiz.objects.create(
                type=cd['type'],
                genre=cd['genre'],
                name=cd['name'],
            )
            for option in cd['option']:
                _option = answer.objects.create(
                    name=option.name,
                    correct=option.correct,
                )
                _quiz.add(_option)
            _quiz.save()
    else:
        genres = genre.objects.all()
        types = type.objects.all()
        return render(request, 'import.html', {"genres": genres, "types": types})
