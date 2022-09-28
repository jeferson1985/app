from django.db import models


class Medicamentos(models.Model):
    name = models.CharField(max_length=240)
    price = models.FloatField()
    indications = models.CharField(max_length=240)
    againstIndications = models.CharField(max_length=240)
    adverseReactions= models.CharField(max_length=240)
    precautions = models.CharField(max_length=240)
    
    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['name']