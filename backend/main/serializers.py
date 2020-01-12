from rest_framework import serializers
from .models import *

class UserInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserInfo
        fields = (
            'name',
            'admn_no',
            'degree', 
            'adress',
            'addhar',
            'ph_no',
            'email',
        )
    

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Books
        fields = (
            'name',
            'issued_date',
            'issued_by',
            'is_issued',
        )