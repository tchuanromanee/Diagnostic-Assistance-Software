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
    #     return self.pub_date >= timezone.now() - datetime.timedelta(days=1c

	
class  Diagsymp(models.Model): # Relates which diagnoses has which symptoms
	linkID = models.AutoField(primary_key=True)
	diagID = models.ForeignKey(Diagnoses, on_delete=models.CASCADE)
	symp1 = models.IntegerField()
	prevalent1 = models.BooleanField()
	symp2 = models.IntegerField()
	prevalent2 = models.BooleanField()
	symp3 = models.IntegerField()
	prevalent3 = models.BooleanField()
	symp4 = models.IntegerField()
	prevalent4 = models.BooleanField()
	symp5 = models.IntegerField()
	prevalent5 = models.BooleanField()
	symp6 = models.IntegerField()
	prevalent6 = models.BooleanField()

class DiffDiag(models.Model): # Relates each diagnosis to a differential diagnostic
	diffID = models.AutoField(primary_key=True)
	diagnosis = models.ForeignKey(Diagnoses, on_delete=models.CASCADE, related_name='diagnosis')
	differentialDiagnosis = models.ForeignKey(Diagnoses, on_delete=models.CASCADE, related_name='differentialDiagnosis')

class Symptoms(models.Model):
	sympID = models.AutoField(primary_key=True)
	name = models.CharField(max_length=500)
# class Choice(models.Model):
#     diagnosis = models.ForeignKey(Diagnoses, on_delete=models.CASCADE)
#     choice_text = models.CharField(max_length=200)
#     votes = models.IntegerField(default=0)
#     def __str__(self):
#         return self.choice_text
