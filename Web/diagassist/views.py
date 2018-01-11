from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
# Create your views here.
from .models import Therapist, Symptom, Diagnostic


# class IndexView(generic.ListView):
# return HttpResponse(html)

def indexView(request):
	template_name = 'index.html'
	return render(request, template_name)
	
def loginView(request):
	template_name = 'login.html'
	return render(request, template_name)
	
def signupView(request):
	template_name = 'signup.html'
	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			raw_password = form.cleaned_data.get('password1')
			user = authenticate(username=username, password=raw_password)
			login(request, user)
			return redirect('home')
	else:
		form = UserCreationForm()
	return render(request, template_name, {'form': form})	

# Create your views here.
def update_profile(request, user_id):
    user = User.objects.get(pk=user_id)
    user.therapist.phone = 1234567890
    user.save()