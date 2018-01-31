from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from dal import autocomplete
from .models import Diagnostic


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
	preexisting = forms.ModelMultipleChoiceField(queryset=Diagnostic.objects.all())
	# Symptom 1
	# Persistent 1
	#first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
	#last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
	#email = forms.EmailField(max_length=254, help_text='Required.')
	class Meta:
		model = Diagnostic
		fields = ('__all__')
		widgets = {
			'name': autocomplete.ModelSelect2(url='diagnose')
		}