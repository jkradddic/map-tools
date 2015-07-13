from django.db import models
from django.contrib.gis.db import models as geomodels



class Map(geomodels.Model):
	name = models.CharField(max_length=256)
	notes = models.CharField(max_length=1024, blank=True)
	creator = models.EmailField
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

class MapPoint(geomodels.Model):
	map = models.ForeignKey(Map, related_name = 'points')
	name = models.CharField(max_length=256)
	point = geomodels.PointField()

	objects = geomodels.GeoManager()

	
