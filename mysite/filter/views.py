from django.shortcuts import render
from django.http import HttpResponse
from filter.models import camera

# Create your views here.
def filter(request):
	#Establishing filter constraints
	pIRange = (0,1)
	latRange = (-90, 90)
	longRange = (-180, 180)
	numFloorsGTE = 0
	floorAreaGTE = 0
	totalFloorAreaGTE = 0
	#context = RequestContext(request)
	#category_list = camera.objects.all() #_meta.get_fields() #.order_by("caseID")
	querysets=camera.objects.filter(latitude__range=latRange, longitude__range=longRange, priorityIndex__range=pIRange, numFloors__gte=numFloorsGTE, floorArea_m2__gte=floorAreaGTE, totalFloorArea_m2__gte=totalFloorAreaGTE).order_by("caseID")
	#context_dict = {'categories': category_list}
	columnHeaders = ['CaseID', 'Latitude', 'Longitude', 'Number of Floors']
	return render(request, 'filterIndex.html', {'querysets':querysets,'columnHeaders':columnHeaders})#=context_dict)#, context)
	#return render_to_response('filterIndex.html', context_dict, context) #context=fieldsInFilterModel)

