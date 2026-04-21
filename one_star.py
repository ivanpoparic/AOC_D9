"""
# libraries
# -----------------------------------------
import operator
from math import sqrt

from data import list_of_coords
#from test_data import list_of_coords

# classes
# ---------------------------------------
class RedCorner:
    def __init__(self, id, x_coord, y_coord):
        self.id = id
        self.x_coord = x_coord
        self.y_coord = y_coord

class Rectangle:
    def __init__(self, area, primary_corner, secondary_corner):
        self.area = area
        self.primary_corner = primary_corner
        self.secondary_corner = secondary_corner


# functions
# ---------------------------------------
def calculate_area(corner_object_01, corner_object_02):
    return (abs(corner_object_01.x_coord - corner_object_02.x_coord)+1)*(abs(corner_object_01.y_coord - corner_object_02.y_coord)+1)


# ******************************************
# BEGIN MAIN
# ******************************************

# initializing variables
# -----------------------------------------
final_score = 0
red_corner_object_list = []
rectangle_list = []

# - create list of junction box objects with properties of x,y,z coordinates and circuit
for i in range(len(list_of_coords)):
    red_corner_object_list.append(RedCorner(i, list_of_coords[i][0], list_of_coords[i][1]))

for first_corner in red_corner_object_list:
    for second_corner in red_corner_object_list:
        if first_corner.id < second_corner.id:
            rectangle_list.append(Rectangle(calculate_area(first_corner, second_corner), first_corner.id, second_corner.id))



rectangle_list.sort(key=operator.attrgetter('area'), reverse=True)
print(rectangle_list[0].area)
"""

