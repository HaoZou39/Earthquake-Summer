from django.conf.urls import url, include
from django.views.generic import ListView, DetailView
from filter.models import camera
from filter import views as filter_views
#from . import views




urlpatterns = [
	url(r'^$', filter_views.filter, name='filter'),
	url(r'^(?P<pk>\d+)$', DetailView.as_view(model=camera,template_name="image.html"))
 ]
"""
	url(r'^$', ListView.as_view(
		queryset=camera.objects.all().order_by("caseID"),
		queryset=camera.objects.filter(latitude__range=latRange, longitude__range=longRange, priorityIndex__range=pIRange, numFloors__gte=numFloorsGTE, floorArea_m2__gte=floorAreaGTE, totalFloorArea_m2__gte=totalFloorAreaGTE).order_by("caseID"),
		template_name="filterIndex.html")),
"""
	#,
#]
