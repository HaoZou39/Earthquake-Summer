from django import forms
from filter.models import camera
from django.core.exceptions import ValidationError

def validateCSV(value):
	if not value.name.endswith('.csv'):
		if not value.name.endswith('.CSV'):
			raise ValidationError(u'Error! Please use .csv files only!')

class editForm(forms.ModelForm):
	class Meta:
		model = camera
		fields = ('caseID','latitude','longitude','priorityIndex','numFloors','floorArea_m2','totalFloorArea_m2','photo')

class newForm(forms.ModelForm):
	class Meta:
		model = camera
		fields = ('caseID','latitude','longitude','priorityIndex','numFloors','floorArea_m2','totalFloorArea_m2','photo')

class uploadCSVForm(forms.Form):
	csvFile = forms.FileField(required=False,label="",validators=[validateCSV])
