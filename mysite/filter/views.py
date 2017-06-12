from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, Http404
from filter.models import camera
from .forms import editForm, newForm
from datetime import datetime, timezone

# Create your views here.
def filter(request):
	#Establishing filter constraints
	pImin = 0;
	pImax = 99;
	priorityIndexRange = (pImin,pImax)
	latmin = -90;
	latmax = 90;
	latitudeRange = (latmin,latmax)
	longmin = -180;
	longmax = 180;
	longitudeRange = (longmin,longmax)
	numFloorsmin=0
	numFloorsmax=1000
	numFloorsRange = (numFloorsmin,numFloorsmax)	
	floorAreamin=0
	floorAreamax=9999999
	floorArea_m2Range = (floorAreamin,floorAreamax)
	totalFloorAreamin = 0
	totalFloorAreamax = 9999999
	totalFloorArea_m2Range = (totalFloorAreamin,totalFloorAreamax)

	querysets=camera.objects.filter(latitude__range=latitudeRange, longitude__range=longitudeRange, priorityIndex__range=priorityIndexRange, numFloors__range=numFloorsRange, floorArea_m2__range=floorArea_m2Range, totalFloorArea_m2__range=totalFloorArea_m2Range).order_by("caseID")
	columnHeaders = camera._meta.get_fields()
	columnHeaders = list(map(str,columnHeaders))
	columnHeaders = ['{0}'.format(columnHeader.split('.')[2]) for columnHeader in columnHeaders]
	columnHeaders.pop(0) #do not allow filtering by primary key (which is 'id' column in database)
	if(request.POST.get('filter')):
		min1 = request.POST.get('min1');
		max1 = request.POST.get('max1');
		var1 = request.POST.get('filter1');
		exec(var1+'min'+"=min1")
		exec(var1+'max'+"=max1")
		exec(var1+'Range'+"= (eval(var1+'min'),eval(var1+'max'))")

		min2 = request.POST.get('min2');
		max2 = request.POST.get('max2');
		var2 = request.POST.get('filter2');
		exec(var2+'min'+"=min2")
		exec(var2+'max'+"=max2")
		exec(var2+'Range'+"= (eval(var2+'min'),eval(var2+'max'))")

		min3 = request.POST.get('min3');
		max3 = request.POST.get('max3');
		var3 = request.POST.get('filter3');
		exec(var3+'min'+"=min3")
		exec(var3+'max'+"=max3")
		exec(var3+'Range'+"= (eval(var3+'min'),eval(var3+'max'))")

		querysets=camera.objects.filter(latitude__range=latitudeRange, longitude__range=longitudeRange, priorityIndex__range=priorityIndexRange, numFloors__range=numFloorsRange, floorArea_m2__range=floorArea_m2Range, totalFloorArea_m2__range=totalFloorArea_m2Range).order_by("caseID")
	return render(request, 'filterIndex.html', {'querysets':querysets,'columnHeaders':columnHeaders})
	
