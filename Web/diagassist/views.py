from django.shortcuts import render
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.views import generic
from django.utils import timezone
# Create your views here.
from .models import Therapist, Symptom, Diagnostic


class IndexView(generic.ListView):
	template_name = 'index.html'

def indexss(request):
    return render(request, 'index.html')

# Create your views here.
def update_profile(request, user_id):
    user = User.objects.get(pk=user_id)
    user.therapist.phone = 1234567890
    user.save()