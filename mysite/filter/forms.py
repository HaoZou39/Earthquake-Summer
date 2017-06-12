from django import forms
from filter.models import camera

class editForm(forms.Form):
	def __init__(self, *args, **kwargs):
		primaryKey = kwargs.pop('pk')
		super(editForm,self).__init__(*args,**kwargs)
		self.fields['caseID'] = forms.CharField(max_length=10, label='CaseID', initial=str(camera.objects.get(id=primaryKey).caseID))
		self.fields['latitude'] = forms.FloatField(label='Latitude', initial=float(camera.objects.get(id=primaryKey).latitude))
		self.fields['longitude'] = forms.FloatField(label='Longitude', initial=float(camera.objects.get(id=primaryKey).longitude))
		self.fields['priorityIndex'] = forms.FloatField(label='Priority Index', initial=float(camera.objects.get(id=primaryKey).priorityIndex))
		self.fields['numFloors'] = forms.IntegerField(label='Number of Floors', initial=int(camera.objects.get(id=primaryKey).numFloors))
		self.fields['floorArea_m2'] = forms.IntegerField(label='Floor Area (m2)', initial=int(camera.objects.get(id=primaryKey).floorArea_m2))
		self.fields['totalFloorArea_m2'] = forms.IntegerField(label='Total Floor Area (m2)', initial=int(camera.objects.get(id=primaryKey).totalFloorArea_m2))
