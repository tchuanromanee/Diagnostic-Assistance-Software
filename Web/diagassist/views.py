from django.shortcuts import render
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.views import generic
from django.utils import timezone
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
	return render(request, template_name)

# Create your views here.
def update_profile(request, user_id):
    user = User.objects.get(pk=user_id)
    user.therapist.phone = 1234567890
    user.save()