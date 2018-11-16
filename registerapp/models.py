from django.db import models

class regmodel(models.Model):
    fname=models.CharField(max_length=20)
    lname=models.CharField(max_length=20)
    email=models.EmailField(max_length=20)
    username=models.CharField(max_length=20)
    password=models.CharField(max_length=20)
    contact=models.IntegerField()
    GENDER = (('M', 'Male'), ('F', 'Female'), ('O', 'Other'))
    gender = models.CharField(max_length=1, choices=GENDER, null=True)






