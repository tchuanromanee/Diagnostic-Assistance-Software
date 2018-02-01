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
	class Meta:
		model = Diagnostic
		fields = ('diagID', 'name')

class DiagnoseSympForm(forms.Form):
	# Symptom 1
	symp1 = forms.ModelChoiceField(queryset=Symptom.objects.all(), label='Symptom 1')
	# Persistent 1
	persistent1 = forms.BooleanField(label='Symptom 1 Persistent?')
	# Symptom 2
	symp2 = forms.ModelChoiceField(queryset=Symptom.objects.all(), label='Symptom 2')
	# Persistent 2
	persistent2 = forms.BooleanField(label='Symptom 2 Persistent?')
	# Symptom 3
	symp3 = forms.ModelChoiceField(queryset=Symptom.objects.all(), label='Symptom 3')
	# Persistent 3
	persistent3 = forms.BooleanField(label='Symptom 3 Persistent?')
	# Symptom 4
	symp4 = forms.ModelChoiceField(queryset=Symptom.objects.all(), label='Symptom 4')
	# Persistent 4
	persistent4 = forms.BooleanField(label='Symptom 4 Persistent?')
	# Symptom 5
	symp5 = forms.ModelChoiceField(queryset=Symptom.objects.all(), label='Symptom 5')
	# Persistent 5
	persistent5 = forms.BooleanField(label='Symptom 5 Persistent?')
	# Symptom 6
	symp6 = forms.ModelChoiceField(queryset=Symptom.objects.all(), label='Symptom 6')
	# Persistent 6
	persistent6 = forms.BooleanField(label='Symptom 6 Persistent?')
	#first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
	#last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
	#email = forms.EmailField(max_length=254, help_text='Required.')
	class Meta:
		model = Symptom
		fields = ('sympNumber','name')