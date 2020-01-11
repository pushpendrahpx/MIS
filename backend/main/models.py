from django.db import models

class UserInfo(models.Model):
    name = models.CharField(max_length=200)
    admn_no = models.CharField(max_length=8)
    degree = models.CharField(max_length=10)
    adress = models.CharField(max_length=500)
    addhar = models.CharField(max_length=12)
    ph_no = models.CharField(max_length=10)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
