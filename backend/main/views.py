from django.shortcuts import render
from rest_framework import viewsets, permissions
from .models import *
from .serializers import *
from django.http import JsonResponse
from django.core import serializers
import json

from django.views.decorators.csrf import ensure_csrf_cookie

class UserInfoView(viewsets.ModelViewSet):
    queryset = UserInfo.objects.all()
    serializer_class = UserInfoSerializer
    permission_class = (permissions.IsAuthenticatedOrReadOnly)


class BooksView(viewsets.ModelViewSet):
    queryset = Books.objects.all()
    serializer_class = BookSerializer
    permission_class = (permissions.IsAuthenticatedOrReadOnly)

@ensure_csrf_cookie
def get_user(request):
    if request.method == 'POST':
        print(request.POST['phone'])
        ls = UserInfo.objects.all()
        ls_seiral = serializers.serialize('json', ls)
        json_data = json.dumps(ls_seiral)
        json_data = json.loads(json_data)
        json_data = json.loads(json_data)
        return JsonResponse(json_data, safe=False)
    else:
        return JsonResponse('{"name":"Failed POST bro, it is GET"}',safe=False)
    

def json_create_user(request):
    ls = UserInfo.objects.all()
    if request.method == 'POST':   
        # name = str(request.POST['name'])
        phone = int(request.POST['phone']) 
        ls_seiral = serializers.serialize('json', ls)
        json_data = json.dumps(ls_seiral)
        json_data = json.loads(json_data)
        json_data = json.loads(json_data)
        json_data = '{"name":"GVHJBN"}'
        u = UserInfo(**json_data)
        u.save()
        
    else:
        json_data = ''
    return JsonResponse(json_data, safe=False)


def json_create_books(request):
    ls = Books.objects.all()
    ls_seiral = serializers.serialize('json', ls)
    json_data = json.dumps(ls_seiral)
    json_data = json.loads(json_data)
    json_data = json.loads(json_data)
    return JsonResponse(json_data, safe=False)
    
