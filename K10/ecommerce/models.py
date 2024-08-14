from django.db import models

class Ecommerce(models.Model):
    name=models.CharField(max_length=20)
    number = models.IntegerField()
    email=models.EmailField()

    def __str__(self):
        return self.name
        