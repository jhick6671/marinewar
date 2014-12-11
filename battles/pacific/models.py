from django.contrib.gis.db import models

# Create your models here.
class Battle(models.Model):
    """docstring here"""
    name = models.CharField(max_length=60)
    geom = models.GeometryField()
    objects = models.GeoManager()
    desc = models.CharField(max_length=500, blank=True)

    def __str__(self):
        return"{}-{}".format(self.pk, self.name)

class PointInterest(models.Model):
    name = models.CharField(max_length=60)
    geom = models.PointField()
    objects = models.GeoManager()
    desc = models.CharField(max_length=500, blank=True)

    def __str__(self):
        return"{}-{}".format(self.pk, self.name)