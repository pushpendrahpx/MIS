from django.db import models


class UserInfo(models.Model):
    name = models.CharField(max_length=200)
    admn_no = models.CharField(max_length=8, unique=True)
    degree = models.CharField(max_length=10)
    adress = models.CharField(max_length=500)
    addhar = models.CharField(max_length=12)
    ph_no = models.CharField(max_length=10)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.admn_no


class Books(models.Model):
    name = models.CharField(max_length=500)
    issued_date = models.DateField(default=None, null=True)
    issued_by = models.ForeignKey(UserInfo, to_field='admn_no' , on_delete=models.CASCADE, default=None, null=True)
    is_issued = models.BooleanField()


    def __str__(self):
        return self.name





