from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
# Create your views here.
from .models import Therapist, Symptom, Diagnostic
from diagassist.forms import SignUpForm, DiagnoseForm
from django.contrib.auth.decorators import login_required


# class IndexView(generic.ListView):
# return HttpResponse(html)

def indexView(request):
	template_name = 'index.html'
	return render(request, template_name)
	
def diagnoseView(request):
	template_name = 'diagnose.html'
	if request.method == 'POST':
		form = DiagnoseForm(request.POST)
		if form.is_valid():
			form.save()
			#username = form.cleaned_data.get('username')
			#raw_password = form.cleaned_data.get('password1')
			# Call function to diagnose
			return redirect('/diagassist/')
	else:
		form = DiagnoseForm()
	return render(request, template_name, {'form': form})	

def loginView(request):
	template_name = 'login.html'
	message = 'Please sign in'
	form = AuthenticationForm(request.POST)
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(username=username, password=password)
		if user is not None:
			login(request, user)
			return HttpResponseRedirect('/diagassist/')
		else:
			message = 'Invalid login, please try again.'
	context = {'message': message, 'form': form}
	return render(request, template_name, context)
	
@login_required()
def logoutView(request):
	logout(request)
    # Redirect to a success page.
	return HttpResponseRedirect('/diagassist/logout-success/')

def logoutSuccessView(request):
	template_name = 'logout.html'
	return render(request, template_name)

def signupSuccessView(request):
	template_name = 'signup-success.html'
	return render(request, template_name)
	
def signupView(request):
	template_name = 'signup.html'
	if request.method == 'POST':
		form = SignUpForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			raw_password = form.cleaned_data.get('password1')
			user = authenticate(username=username, password=raw_password)
			login(request, user)
			return redirect('/diagassist/signup-success/')
	else:
		form = SignUpForm()
	return render(request, template_name, {'form': form})	

# Create your views here.
def update_profile(request, user_id):
    user = User.objects.get(pk=user_id)
    user.therapist.phone = 1234567890
    user.save()