from django.db import models

# Create your models here.
class KoffieMachine(models.Model):
    name = models.CharField(max_length=100)
    serial_nomber = models.CharField(max_length=50)
    description = models.CharField(max_length=500)
    # point



class MaintainsHistory(models.Model):
    pass