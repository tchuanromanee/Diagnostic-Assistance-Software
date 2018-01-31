from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from dal import autocomplete
from .models import Diagnostic

from . import views
app_name = 'diagassist'
urlpatterns = [
    # ex: /diagassist/
	url(r'^$', views.indexView, name='index-view'),
     # ex: /diagassist/signup/
    url(r'^signup/$', views.signupView, name='signup-view'),
	# ex: /diagassist/login/
    url(r'^login/$', views.loginView, name='login-view'),
	# ex: /diagassist/logout/
    url(r'^logout/$', views.logoutView, name='logout-view'),
    url(r'^logout-success/$', views.logoutSuccessView, name='logout-success-view'),
    url(r'^signup-success/$', views.signupSuccessView, name='signup-success-view'),
	# ex: /diagassist/diagnose/
    url(r'^diagnose/$', views.diagnoseView, name='diagnose-view')
    # ex: /polls/5/results/
    #url(r'^(?P<pk>[0-9]+)/results/$', views.ResultsView.as_view(), name='results'),
    # ex: /polls/5/vote/
    #url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
]
