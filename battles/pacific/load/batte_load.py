import shapefile
import json
from battles.pacific.models import Battle
import django
django.setup()

battle_path = 'C:/Users/jhick6671/PycharmProjects/marinewar/battles/pacific/load/POLYGON2.shp'

sf = shapefile.Reader(battle_path)
battles = sf.shapeRecords()

for r in battles:
    battle_poly = r.shape.__geo_interface__
    m = Battle(name=r.record[-1].title(),
               geom=json.dumps(battle_poly))
    m.save()