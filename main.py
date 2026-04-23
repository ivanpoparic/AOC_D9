# libraries
# -----------------------------------------
import operator
from math import sqrt

from data import list_of_coords
#from test_data import list_of_coords


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


class HorizontalLine:
    def __init__(self, x_low, x_high, y):
        self.x_low = x_low
        self.x_high = x_high
        self.y = y


class VerticalLine:
    def __init__(self, y_low, y_high, x):
        self.y_low = y_low
        self.y_high = y_high
        self.x = x

# functions
# ---------------------------------------
def calculate_area(corner_object_01, corner_object_02):
    return (abs(corner_object_01.x_coord - corner_object_02.x_coord) + 1) * (
                abs(corner_object_01.y_coord - corner_object_02.y_coord) + 1)

def is_in_total_area(x, y):
    if [x, y] in list_of_coords:
        return True
    elif is_point_on_line(x, y):
        return True
    elif is_point_between_marks(x, y):
        return True
    return False

def is_point_on_line(x, y):
    for line in horizontal_line_list:
        if y == line.y and line.x_low <= x <= line.x_high:
            return True
    for line in vertical_line_list:
        if x == line.x and line.y_low <= y <= line.y_high:
            return True
    return False

def is_point_between_marks(x, y):
    if is_horizontal_line_below(x, y) and is_horizontal_line_above(x, y) and is_vertical_line_left(x,y) and is_vertical_line_right(x, y):
        return True
    return False

def is_horizontal_line_below(x, y):
    for line in horizontal_line_list:
        if line.x_low <= x <= line.x_high:
            if line.y <= y:
                return True
    return False

def is_horizontal_line_above(x, y):
    for line in horizontal_line_list:
        if line.x_low <= x <= line.x_high:
            if line.y >= y:
                return True
    return False

def is_vertical_line_left(x, y):
    for line in vertical_line_list:
        if line.y_low <= y <= line.y_high:
            if line.x <= x:
                return True
    return False


def is_vertical_line_right(x, y):
    for line in vertical_line_list:
        if line.y_low <= y <= line.y_high:
            if line.x >= x:
                return True
    return False

def is_each_point_on_rectangle_between(corner_object_01, corner_object_02):
    if corner_object_01.x_coord > corner_object_02.x_coord:
        x_min = corner_object_02.x_coord
        x_max = corner_object_01.x_coord
    else:
        x_min = corner_object_01.x_coord
        x_max = corner_object_02.x_coord
    if corner_object_01.y_coord > corner_object_02.y_coord:
        y_min = corner_object_02.y_coord
        y_max = corner_object_01.y_coord
    else:
        y_min = corner_object_01.y_coord
        y_max = corner_object_02.y_coord

    for point in range(y_min, y_max + 1, 1000):
        if not is_in_total_area(x_min, point):
            return False
        if not is_in_total_area(x_max, point):
            return False
    for point in range(x_min, x_max + 1, 1000):
        if not is_in_total_area(point, y_min):
            return False
        if not is_in_total_area(point, y_max):
            return False

    for point in range(y_min, y_max + 1, 100):
        if not is_in_total_area(x_min, point):
            return False
        if not is_in_total_area(x_max, point):
            return False
    for point in range(x_min, x_max + 1, 100):
        if not is_in_total_area(point, y_min):
            return False
        if not is_in_total_area(point, y_max):
            return False

    for point in range(y_min, y_max + 1):
        if not is_in_total_area(x_min, point):
            return False
        if not is_in_total_area(x_max, point):
            return False
    for point in range(x_min, x_max + 1):
        if not is_in_total_area(point, y_min):
            return False
        if not is_in_total_area(point, y_max):
            return False

    return True


#Prvi crveni je na 7,1. Drugi crveni je na 9,5
#Njihov prvi zeleni je na 7,5. Drugi zeleni je na 9,1



# ******************************************
# BEGIN MAIN
# ******************************************

# initializing variables
# -----------------------------------------
final_score = 0
red_corner_object_list = []
green_corner_object_list = []
vertical_line_list = []
horizontal_line_list = []
rectangle_list = []

# - create list of red corner objects with properties of x,y,
for i in range(len(list_of_coords)):
    red_corner_object_list.append(RedCorner(i, list_of_coords[i][0], list_of_coords[i][1], 0))
    if i < (len(list_of_coords) - 1):
        if list_of_coords[i][0] == list_of_coords[i + 1][0]:
            # vertikalna dužina (barem po primjeru)
            if list_of_coords[i][1] > list_of_coords[i + 1][1]:
                vertical_line_list.append(
                    VerticalLine(list_of_coords[i + 1][1], list_of_coords[i][1], list_of_coords[i][0]))
            else:
                vertical_line_list.append(
                    VerticalLine(list_of_coords[i][1], list_of_coords[i + 1][1], list_of_coords[i][0]))
        elif list_of_coords[i][1] == list_of_coords[i + 1][1]:
            # horizontalna dužina (barem po primjeru)
            if list_of_coords[i][0] > list_of_coords[i + 1][0]:
                horizontal_line_list.append(
                    HorizontalLine(list_of_coords[i + 1][0], list_of_coords[i][0], list_of_coords[i][1]))
            else:
                horizontal_line_list.append(
                    HorizontalLine(list_of_coords[i][0], list_of_coords[i + 1][0], list_of_coords[i][1]))
    elif i == (len(list_of_coords) - 1):
        if list_of_coords[i][0] == list_of_coords[0][0]:
            # vertikalna dužina (barem po primjeru)
            if list_of_coords[i][1] > list_of_coords[0][1]:
                vertical_line_list.append(
                    VerticalLine(list_of_coords[0][1], list_of_coords[i][1], list_of_coords[i][0]))
            else:
                vertical_line_list.append(
                    VerticalLine(list_of_coords[i][1], list_of_coords[0][1], list_of_coords[i][0]))
        elif list_of_coords[i][1] == list_of_coords[0][1]:
            # horizontalna dužina (barem po primjeru)
            if list_of_coords[i][0] > list_of_coords[0][0]:
                horizontal_line_list.append(
                    HorizontalLine(list_of_coords[0][0], list_of_coords[i][0], list_of_coords[i][1]))
            else:
                horizontal_line_list.append(
                    HorizontalLine(list_of_coords[i][0], list_of_coords[0][0], list_of_coords[i][1]))
horizontal_line_list.sort(key=lambda x: x.y)
vertical_line_list.sort(key=lambda x: x.x)

"""
small_pair = []
for i in range(10):
    for j in range(15):
        small_pair = [j, i]
        if small_pair in list_of_coords:
            print("#", sep="", end="")
        elif is_point_on_line(j, i):
            print("X", sep="", end="")

        elif is_point_between_marks(j, i):
            print("x", sep="", end="")
        #           elif j==9 and i==3:
        #                print("M",sep="",end="")
        else:
            print(".", sep="", end="")
    print("\n", sep="", end="")
"""
nm_of_total_checked = 0
nm_of_good_ones_checked = 0

for first_corner in red_corner_object_list:
    for second_corner in red_corner_object_list:
        if first_corner.id < second_corner.id:
            nm_of_total_checked += 1
            if is_each_point_on_rectangle_between(first_corner, second_corner):
                rectangle_list.append(Rectangle(calculate_area(first_corner, second_corner), first_corner.id, second_corner.id))
                nm_of_good_ones_checked+=1
                print(f"Ovaj se računa.. Zasad {nm_of_good_ones_checked}/{nm_of_total_checked}")










rectangle_list.sort(key=operator.attrgetter('area'), reverse=True)
print(f"Najveći je {rectangle_list[0].area}, započet od [{red_corner_object_list[rectangle_list[0].primary_corner].x_coord},{red_corner_object_list[rectangle_list[0].primary_corner].y_coord}] i [{red_corner_object_list[rectangle_list[0].secondary_corner].x_coord},{red_corner_object_list[rectangle_list[0].secondary_corner].y_coord}]")
print(rectangle_list[0].area)

print(f"Od ukupno {nm_of_total_checked} bilo je dobrih {nm_of_good_ones_checked}")


