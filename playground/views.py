from django.shortcuts import render
from django.http import HttpResponse
from .operation import Operation as op
import json
from django.core import serializers
# Create your views here.


def verify(request):
    return HttpResponse(op.verify_tweepy())


def getUser(request):

    verifiedObject = op.getObject()

    user = op.getUser(verifiedObject)
    response_data = json.dumps(user._json)

    return HttpResponse((response_data), content_type="application/json")


def operation1(request):
    return HttpResponse(('operation1'), content_type="application/json")


def operation2(request):
    return HttpResponse(('operation2'), content_type="application/json")


def operation3(request):
    return HttpResponse(('operation3'), content_type="application/json")


def operation4(request):
    return HttpResponse(('operation4'), content_type="application/json")


def operation5(request):
    return HttpResponse(('operation5'), content_type="application/json")


def operation6(request):
    return HttpResponse(('operation6'), content_type="application/json")


def operation7(request):
    return HttpResponse(('operation7'), content_type="application/json")


def operation8(request):
    return HttpResponse(('operation8'), content_type="application/json")


def operation9(request):
    return HttpResponse(('operation9'), content_type="application/json")


def operation10(request):
    return HttpResponse(('operation10'), content_type="application/json")


def operation11(request):
    return HttpResponse(('operation11'), content_type="application/json")


def operation12(request):
    return HttpResponse(('operation12'), content_type="application/json")


def operation13(request):
    return HttpResponse(('operation13'), content_type="application/json")
