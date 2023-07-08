from django.shortcuts import render,HttpResponse
from rest_framework.decorators import api_view
from .utils import *

# Create your views here.
@api_view(['GET'])
def first(request):
    return HttpResponse({"HO":1})

@api_view(['POST'])
def upload_view(request):
    res=upload_utils(request)
    return res