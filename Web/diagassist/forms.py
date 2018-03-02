from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from dal import autocomplete
from .models import Diagnostic, Symptom


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required.')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )

genderChoices = [
	(0, 'Male'),
	(1, 'Female'),
	(2, 'Other'),
	]

class DiagnoseForm(forms.Form):
	# Gender
	gender = forms.CharField(label='Patient gender', widget=forms.Select(choices=genderChoices))
	# Age
	age = forms.IntegerField()
	# Pre-existing Conditions
	preexisting = forms.ModelMultipleChoiceField(queryset=Diagnostic.objects.all(), label='Pre-existing Condition')
	#first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
	#last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
	#email = forms.EmailField(max_length=254, help_text='Required.')
	# Symptom 1
	symp1 = forms.ModelChoiceField(queryset=Symptom.objects.values('sympID', 'name'), label='Symptom 1')
	# Persistent 1
	persistent1 = forms.BooleanField(label='Symptom 1 Persistent?', required=False)
	# Symptom 2
	symp2 = forms.ModelChoiceField(queryset=Symptom.objects.all(), label='Symptom 2', required=False)
	# Persistent 2
	persistent2 = forms.BooleanField(label='Symptom 2 Persistent?', required=False)
	# Symptom 3
	symp3 = forms.ModelChoiceField(queryset=Symptom.objects.all(), label='Symptom 3', required=False)
	# Persistent 3
	persistent3 = forms.BooleanField(label='Symptom 3 Persistent?', required=False)
	# Symptom 4
	symp4 = forms.ModelChoiceField(queryset=Symptom.objects.all(), label='Symptom 4', required=False)
	# Persistent 4
	persistent4 = forms.BooleanField(label='Symptom 4 Persistent?', required=False)
	# Symptom 5
	symp5 = forms.ModelChoiceField(queryset=Symptom.objects.all(), label='Symptom 5', required=False)
	# Persistent 5
	persistent5 = forms.BooleanField(label='Symptom 5 Persistent?', required=False)
	# Symptom 6
	symp6 = forms.ModelChoiceField(queryset=Symptom.objects.all(), label='Symptom 6', required=False)
	# Persistent 6
	persistent6 = forms.BooleanField(label='Symptom 6 Persistent?', required=False)


def processDiagnosis():
	modelInputs = []