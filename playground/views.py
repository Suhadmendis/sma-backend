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
    
   
    
    
    
    # operation = Operation("fdsfs", "23")
    
    return HttpResponse((response_data), content_type="application/json")