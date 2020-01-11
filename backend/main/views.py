from django.shortcuts import render
from rest_framework import viewsets
from .models import *
from .serializers import *
from django.http import JsonResponse
from django.core import serializers
import json
class UserInfoView(viewsets.ModelViewSet):
    queryset = UserInfo.objects.all()
    serializers_class = UserInfoSerializer

def json_create(request):
    ls = UserInfo.objects.all()
    ls_seiral = serializers.serialize('json', ls)
    json_data = json.dumps(ls_seiral)
    json_data = json.loads(json_data)
    json_data = json.loads(json_data)
    return JsonResponse(json_data, safe=False)

    
