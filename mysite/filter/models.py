from django.db import models
from datetime import datetime

class camera(models.Model):
	caseID = models.CharField(max_length=10) #Some case IDs are longer than 3 digits. Max length of 10 to be safe. Maybe remove this constraint?
	latitude = models.FloatField()
	longitude = models.FloatField()
	priorityIndex = models.FloatField()
	numFloors = models.PositiveIntegerField(default=0)
	floorArea_m2 = models.PositiveIntegerField(default=0)
	totalFloorArea_m2 = models.PositiveIntegerField(default=0)
	lastModifiedUser = models.CharField(max_length=140, default="")
	lastModifiedDate = models.CharField(default=str(datetime.now), max_length=100)

	def __str__(self):
		return self.caseID

