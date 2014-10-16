from battles.pacific import models
from rest_framework import serializers
from rest_framework_gis import serializers as geoserializers

class BattleSerializer(geoserializers.GeoFeatureModelSerializer):
    class Meta:
        model = models.Battle
        geo_field = 'geom'
        fields = ('id', 'name')
