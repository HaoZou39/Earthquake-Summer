from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, Http404
from filter.models import camera
from .forms import editForm, newForm
from datetime import datetime, timezone

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
	image = get_object_or_404(camera, pk=pk)
	if request.method == 'POST':
		form = editForm(request.POST, instance=image)
		if form.is_valid():
			image = form.save(commit=False)
			image.lastModifiedUser = str(request.user)
			image.lastModifiedDate = str(datetime.now)
			image.save()
			return redirect('filter')
	else:
		form = editForm(instance=image)
	return render(request, 'filterEdit.html', {'form':form})

def newImage(request):
	if request.method == 'POST':
		form = newForm(request.POST)
	else:
		form = newForm()
	if form.is_valid():
		image = form.save(commit=False)
		image.lastModifiedUser = str(request.user)
		image.lastModifiedDate = str(datetime.now)
		image.save()
		return redirect('filter')
	return render(request, 'filterEdit.html', {'form':form})

def deleteImage(request, pk):
	imageToDelete = camera.objects.get(id=pk)
	imageToDelete.delete()
	return HttpResponseRedirect('/filter/')
