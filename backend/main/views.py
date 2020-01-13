from django.shortcuts import render, redirect
from rest_framework import viewsets, permissions
from .models import *
from .serializers import *
from django.http import JsonResponse
from django.core import serializers
from  django.contrib.auth.models import User, auth 
import json
from rest_framework.response import Response
from rest_framework.views import APIView
 

class UserInfoView(viewsets.ModelViewSet):
    queryset = UserInfo.objects.all()
    serializer_class = UserInfoSerializer
    permission_class = (permissions.IsAuthenticatedOrReadOnly)


class BooksView(viewsets.ModelViewSet):
    queryset = Books.objects.all()
    serializer_class = BookSerializer
    permission_class = (permissions.IsAuthenticatedOrReadOnly)


def json_create_user(request):
    ls = UserInfo.objects.all()
    if request.method == 'POST':    
        serializer = UserInfoSerializer(data = request.da)
        if serializer.is_valid():
            serializer.save()
            ls_seiral = serializers.serialize('json', ls)
            json_data = json.dumps(ls_seiral)
            json_data = json.loads(json_data)
            json_data = json.loads(json_data)
            return Response(serializer.data, status=200)   
    else:
        json_data = {}
    return JsonResponse(json_data, safe=False)


def json_create_books(request):
    ls = Books.objects.all()
    ls_seiral = serializers.serialize('json', ls)
    json_data = json.dumps(ls_seiral)
    json_data = json.loads(json_data)
    json_data = json.loads(json_data)
    return JsonResponse(json_data, safe=False)
    
