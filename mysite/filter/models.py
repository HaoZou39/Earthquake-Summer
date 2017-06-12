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







"""
	#id = models.PositiveIntegerField(primary_key=True)
	camera_key = models.CharField(max_length=200)
	encrypted_camera_key = models.CharField(max_length=200)
	type = models.CharField(max_length=10)
	source = models.CharField(max_length=20)
	latitude = models.FloatField()
	longitude = models.FloatField()
	country = models.CharField(max_length=50)
	state = models.CharField(max_length=30)
	city = models.CharField(max_length=30)
	resolution_width = models.PositiveSmallIntegerField()
	resolution_height = models.PositiveSmallIntegerField()mo
	frame_rate = models.FloatField()
	is_video = models.BooleanField()
	is_active = models.BooleanField()          
	is_safe = models.BooleanField()
	is_high_load = models.BooleanField()
	is_analysis_restricted = models.BooleanField()
	utc_offset = models.IntegerField()      
	timezone_id = models.CharField(max_length=50)
	timezone_name = models.CharField(max_length=100)
	inactive_since = models.DateTimeField()
	inactive_count = models.PositiveSmallIntegerField()
	reference_logo = models.CharField(max_length=20)
	reference_url = models.CharField(max_length=250)
	last_updated = models.DateTimeField()
	multiple_cameras = models.IntegerField()
	is_located = models.IntegerField()
	weather_wind_speed = models.IntegerField()
	weather_temperature_faren = models.IntegerField()
	weather_humidity = models.IntegerField()
	weather_code = models.IntegerField()            
	shared_id = models.PositiveIntegerField()
	marked = models.BooleanField()
	weather_code_name = models.CharField(max_length=50)
	indoor_outdoor_user = models.BooleanField()
	indoor_outdoor_program = models.BooleanField()
	IN_LOCATION_BOOLEAN = (
		('Y', 'Yes'),
		('N', 'No'),
	)
	in_location = models.CharField(max_length=1, choices=IN_LOCATION_BOOLEAN)
	local_snapshot = models.CharField(max_length=20)
	local_snapshot_date = models.DateTimeField()

	def __str__(self):
		return str(self.camera_key)
"""
	

