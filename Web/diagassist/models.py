from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser, User
from django.db.models.signals import post_save
from django.dispatch import receiver
import datetime
from decimal import Decimal


class Diagnostic(models.Model):
    diagID = models.AutoField(primary_key=True)
    ICD9 = models.DecimalField(max_digits=6, decimal_places=2)
    ICD10 = models.CharField(max_length=10)
    page = models.PositiveIntegerField()
    name = models.CharField(max_length=150)
    def __str__(self):
        return self.name
    # def was_published_recently(self):
    #     return self.pub_date >= timezone.now() - datetime.timedelta(days=1c

	
class Comorbidity(models.Model):
	comorbID = models.AutoField(primary_key=True)
	diagID = models.ForeignKey(Diagnostic, on_delete=models.CASCADE)
	description = models.CharField(max_length=500)
	
class  Diagsymp(models.Model): # Relates which diagnoses has which symptoms
	linkID = models.AutoField(primary_key=True)
	diagID = models.ForeignKey(Diagnostic, on_delete=models.CASCADE)
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
	diagnosis = models.ForeignKey(Diagnostic, on_delete=models.CASCADE, related_name='diagnosis')
	differentialDiagnosis = models.ForeignKey(Diagnostic, on_delete=models.CASCADE, related_name='differentialDiagnosis')

class Symptom(models.Model):
	sympID = models.AutoField(primary_key=True)
	sympNumber = models.DecimalField(max_digits=6, decimal_places=2)
	name = models.CharField(max_length=500)

class Therapist(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	numPatients = models.PositiveIntegerField()
	phone = models.IntegerField()

@receiver(post_save, sender=User)
def create_therapist(sender, instance, created, **kwargs):
    if created:
        Therapist.objects.create(user=instance)

# Commented this out to allow loggin gin
#def save_therapist(sender, instance, **kwargs):
 #   try:
#		instance.therapist.save()
#	except ObjectDoesNotExist:
#		print("nn")
		# profile = Profile(user=request.user)

	
class Client(models.Model):
	clientID = models.AutoField(primary_key=True)
	clientNumber = models.CharField(max_length=10)
	therapistID = models.ForeignKey(Therapist, on_delete=models.CASCADE, default=-1)
	age = models.PositiveIntegerField()
	gender = models.CharField(max_length=1)

class Preexisting(models.Model): # Links clients to preexisting diosrders
	preexistingID = models.AutoField(primary_key=True)
	clientID = models.ForeignKey(Client, on_delete=models.CASCADE)
	diagID = models.ForeignKey(Diagnostic, on_delete=models.CASCADE)

class ClientSymptom(models.Model): # Links clients to their symptoms
	clientSympID = models.AutoField(primary_key=True)
	clientID = models.ForeignKey(Client, on_delete=models.CASCADE)
	sympID = models.ForeignKey(Symptom, on_delete=models.CASCADE)