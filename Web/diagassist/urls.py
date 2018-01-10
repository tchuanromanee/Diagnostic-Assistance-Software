from django.conf.urls import url

from . import views
app_name = 'diagassist'
urlpatterns = [
    # ex: /diagassist/
	url(r'^$', views.indexView, name='main-view'),
     # ex: /diagassist/signup/
    url(r'^signup/$', views.signupView, name='signup')
    # ex: /polls/5/results/
    #url(r'^(?P<pk>[0-9]+)/results/$', views.ResultsView.as_view(), name='results'),
    # ex: /polls/5/vote/
    #url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
]
