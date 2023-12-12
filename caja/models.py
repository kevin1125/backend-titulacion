from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Caja(models.Model):
     User = models.ForeignKey(User,null=True,blank=True,on_delete=models.CASCADE)

class Meta:
        db_table = 'Caja' 