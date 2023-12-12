from django.db import models

# Create your models here.
class Plan(models.Model):
    meses_diferidos = models.CharField(max_length=100,primary_key=True)

    def __str__(self):
        return self.meses_diferidos
    
    class Meta:
        db_table = 'Plan' 