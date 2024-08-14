from django.db import models
class Item(models.Model):
    Pid=models.IntegerField()
    Pname=models.CharField(max_length=20)
    Pprice=models.FloatField()
    Pimg=models.ImageField(upload_to='images/')
    Pmfg=models.DateField()
   