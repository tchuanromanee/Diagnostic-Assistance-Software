from django.db import models
from django.utils import timezone

import datetime

# Create your models here.
class Diagnoses(models.Model):
    diagID = models.AutoField(primary_key=True)
    ICD9 = models.DecimalField(max_digits=6, decimal_places=2)
    ICD10 = models.CharField(max_length=6)
    page = models.IntegerField()
    name = models.CharField(max_length=70)
    def __str__(self):
        return self.name
    # def was_published_recently(self):
    #     return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

# class Choice(models.Model):
#     diagnosis = models.ForeignKey(Diagnoses, on_delete=models.CASCADE)
#     choice_text = models.CharField(max_length=200)
#     votes = models.IntegerField(default=0)
#     def __str__(self):
#         return self.choice_text
