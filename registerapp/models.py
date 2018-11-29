from django.db import models

class regmodel(models.Model):
    fname=models.CharField(max_length=30)
    lname=models.CharField(max_length=30)
    email=models.EmailField(max_length=30)
    username=models.CharField(max_length=30, primary_key=True)
    password=models.CharField(max_length=30)
    contact=models.IntegerField()
    GENDER = (('M', 'Male'), ('F', 'Female'), ('O', 'Other'))
    gender = models.CharField(max_length=1, choices=GENDER, null=True)

class request(models.Model):
    regmo=models.ForeignKey(regmodel,on_delete=True,null=True)
    request=models.CharField(max_length=200, null=True)
    answer=models.CharField(max_length=20, null= True)







