
# libraries
# -----------------------------------------
import operator
from math import sqrt

#from data import list_of_coords
from test_data import list_of_coords

# classes
# ---------------------------------------
class RedCorner:
    def __init__(self, id, x_coord, y_coord, neighbours):
        self.id = id
        self.x_coord = x_coord
        self.y_coord = y_coord
        self.neighbours = neighbours

class Rectangle:
    def __init__(self, area, primary_corner, secondary_corner):
        self.area = area
        self.primary_corner = primary_corner
        self.secondary_corner = secondary_corner


# functions
# ---------------------------------------
def calculate_area(corner_object_01, corner_object_02):
    return (abs(corner_object_01.x_coord - corner_object_02.x_coord)+1)*(abs(corner_object_01.y_coord - corner_object_02.y_coord)+1)

def fill_green_in_between_corners(corner_object_1, corner_object_2):
    global green_corner_object_list
    temp_small_pair = []
    if corner_object_1.x_coord == corner_object_2.x_coord:
        if corner_object_1.y_coord > corner_object_2.y_coord:
            y_ll_limit = corner_object_2.y_coord+1
            y_hh_limit = corner_object_1.y_coord+1
        else:
            y_ll_limit = corner_object_1.y_coord+1
            y_hh_limit = corner_object_2.y_coord+1
        temp_small_pair.append(corner_object_1.x_coord)
        for y in range(y_ll_limit, y_hh_limit):
            temp_small_pair.append(y)
            green_corner_object_list.append(temp_small_pair)
            temp_small_pair.remove(y)
        temp_small_pair.remove(corner_object_1.x_coord)
    else:
        if corner_object_1.x_coord > corner_object_2.x_coord:
            x_ll_limit = corner_object_2.x_coord + 1
            x_hh_limit = corner_object_1.x_coord + 1
        else:
            x_ll_limit = corner_object_1.x_coord + 1
            x_hh_limit = corner_object_2.x_coord + 1

        for x in range(x_ll_limit, x_hh_limit):
            temp_small_pair.append(x)
            temp_small_pair.append(corner_object_1.y_coord)
            green_corner_object_list.append(temp_small_pair)
            temp_small_pair.remove(corner_object_1.y_coord)
            temp_small_pair.remove(x)






def calculate_neighbours(corner_object):
    global list_of_coords
    neighbours = 0
    if [corner_object[0]+1, corner_object[1]+1] in list_of_coords:
        neighbours += 1
    if [corner_object[0]+1, corner_object[1]-1] in list_of_coords:
        neighbours += 1
    if [corner_object[0]-1, corner_object[1]+1] in list_of_coords:
        neighbours += 1
    if [corner_object[0]-1, corner_object[1]-1] in list_of_coords:
        neighbours += 1
    return neighbours



# ******************************************
# BEGIN MAIN
# ******************************************

# initializing variables
# -----------------------------------------
final_score = 0
red_corner_object_list = []
green_corner_object_list = []
rectangle_list = []

# - create list of junction box objects with properties of x,y,z coordinates and circuit
for i in range(len(list_of_coords)):
    red_corner_object_list.append(RedCorner(i, list_of_coords[i][0], list_of_coords[i][1], calculate_neighbours(list_of_coords[i])))



for first_corner in red_corner_object_list:
    for second_corner in red_corner_object_list:
        if first_corner.id < second_corner.id:
            fill_green_in_between_corners(first_corner, second_corner)

for green_corner in green_corner_object_list:
    print(green_corner)
print(len(green_corner_object_list))

small_pair=[]
for i in range(10):
        for j in range(15):
            small_pair.append(j)
            small_pair.append(i)
            if small_pair in list_of_coords:
                print("#",sep="",end="")
            elif small_pair in green_corner_object_list:
                print("X",sep="",end="")
            else:
                print(".",sep="",end="")
            small_pair.remove(j)
            small_pair.remove(i)
        print("\n", sep="",end="")




"""
for first_corner in red_corner_object_list:
    for second_corner in red_corner_object_list:
        if first_corner.id < second_corner.id:
            rectangle_list.append(Rectangle(calculate_area(first_corner, second_corner), first_corner.id, second_corner.id))
            
rectangle_list.sort(key=operator.attrgetter('area'), reverse=True)
#print(rectangle_list[0].area)            
            

"""


