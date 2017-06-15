from django import forms
from filter.models import camera

class editForm(forms.ModelForm):
	class Meta:
		model = camera
		fields = ('caseID','latitude','longitude','priorityIndex','numFloors','floorArea_m2','totalFloorArea_m2','photo')

class newForm(forms.ModelForm):
	class Meta:
		model = camera
		fields = ('caseID','latitude','longitude','priorityIndex','numFloors','floorArea_m2','totalFloorArea_m2','photo')
