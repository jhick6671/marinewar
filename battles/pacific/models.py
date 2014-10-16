from django.contrib.gis.db import models

# Create your models here.
class Battle(models.Model):
    """docstring here"""
    name = models.CharField(max_length=60)
    geom = models.MultiPolygonField()
    objects = models.GeoManager()
    desc = models.CharField(max_length=500)

    def __str__(self):
        return"{}".format(self.name)

