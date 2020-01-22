import math

from neighbors.constant import NEIGHBOR_DELTA, EARTH_RADIUS

class OrthodermicAnalyzer:
    def __init__(self, items, reference_location):
        self._items = items
        self._reference_location = reference_location
        self._admissible_items = None
    
    def find_admissible_items(self):
        x, y = self._reference_location
        x, y = math.radians(float(x)), math.radians(float(y))
        admissible_items = []
        for item in self._items:
            xx = math.radians(float(item['latitude']))
            yy = math.radians(float(item['longitude']))
            central_angle = math.acos(
                math.sin(x) * math.sin(xx) + 
                math.cos(x) * math.cos(xx) * math.cos(abs(y - yy))
            ) 
            arc_length = EARTH_RADIUS * central_angle
            if arc_length < NEIGHBOR_DELTA: 
                admissible_items.append(item)
        self._admissible_items = admissible_items

    @property
    def admissible_items(self):
        return self._admissible_items