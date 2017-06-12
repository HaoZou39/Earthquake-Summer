from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, Http404
from filter.models import camera
from .forms import editForm

# Create your views here.
def filter(request):
	#Establishing filter constraints
	pIRange = (0,1)
	latRange = (-90, 90)
	longRange = (-180, 180)
	numFloorsGTE = 0
	floorAreaGTE = 0
	totalFloorAreaGTE = 0
	querysets=camera.objects.filter(latitude__range=latRange, longitude__range=longRange, priorityIndex__range=pIRange, numFloors__gte=numFloorsGTE, floorArea_m2__gte=floorAreaGTE, totalFloorArea_m2__gte=totalFloorAreaGTE).order_by("caseID")
	columnHeaders = camera._meta.get_fields()
	columnHeaders = list(map(str,columnHeaders))
	columnHeaders = ['{0}'.format(columnHeader.split('.')[2]) for columnHeader in columnHeaders]
	columnHeaders.pop(0) #do not allow filtering by primary key (which is 'id' column in database)
	return render(request, 'filterIndex.html', {'querysets':querysets,'columnHeaders':columnHeaders})

def editImage(request, pk):
	form = editForm(pk=pk)
	return render(request, 'filterEdit.html', {'form':form})
