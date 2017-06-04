from django.conf.urls import url, include
from django.views.generic import ListView, DetailView
from filter.models import camera
#from . import views

urlpatterns = [
	#url(r'^$', views.filter, name='filter'),
	url(r'^$', ListView.as_view(queryset=camera.objects.all().order_by("caseID"),template_name="filterIndex.html")),
	url(r'^(?P<pk>\d+)$', DetailView.as_view(model=camera,template_name="image.html")),
]
