#  File: Geometry.py

#  Description: Using OOP to store operations on shape classes

#  Student Name: Preston Cook

#  Student UT EID: plc886

#  Partner Name: N/A

#  Partner UT EID: N/A

#  Course Name: CS 313E

#  Unique Number: N/A

#  Date Created: 12/22/2022

#  Date Last Modified: 12/22/2022

import math


class Point (object):
    # constructor with default values
    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z

    # create a string representation of a Point
    # returns a string of the form (x, y, z)
    def __str__(self):
        return f'({self.x}, {self.y}, {self.z})'

    # get distance to another Point object
    # other is a Point object
    # returns the distance as a floating point number
    def distance(self, other):
        x1, y1, z1 = self.x, self.y, self.z
        x2, y2, z2 = other.x, other.y, other.z

        return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2)

    # test for equality between two points
    # other is a Point object
    # returns a Boolean
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y and self.z == other.z


class Sphere (object):
    # constructor with default values
    def __init__(self, x=0, y=0, z=0, radius=1):
        self.center = Point(x, y, z)
        self.radius = radius

    # returns string representation of a Sphere of the form:
    # Center: (x, y, z), Radius: value
    def __str__(self):
        p = self.center
        return f'Center: ({p.x}, {p.y}, {p.z}), Radius: {self.radius}'

    # compute surface area of Sphere
    # returns a floating point number
    def area(self):
        return 4 * math.pi * self.radius ** 2

    # compute volume of a Sphere
    # returns a floating point number
    def volume(self):
        return (4/3) * math.pi * self.radius ** 3

    # determines if a Point is strictly inside the Sphere
    # p is Point object
    # returns a Boolean
    def is_inside_point(self, p):
        return self.center.distance(p) <= self.radius

    # determine if another Sphere is strictly inside this Sphere
    # other is a Sphere object
    # returns a Boolean
    def is_inside_sphere(self, other):
        if self.radius > other.radius:
            lr, sr = self.radius, other.radius
        else:
            lr, sr = other.radius, self.radius

        dist = self.center.distance(other.center)

        return dist <= lr - sr

    # determine if a Cube is strictly inside this Sphere
    # determine if the eight corners of the Cube are strictly
    # inside the Sphere
    # a_cube is a Cube object
    # returns a Boolean
    def is_inside_cube(self, a_cube):
        for p in a_cube.get_vertices():
            if self.center.distance(p) > self.radius:
                return False
        return True

    # determine if a Cylinder is strictly inside this Sphere
    # a_cyl is a Cylinder object
    # returns a Boolean
    def is_inside_cyl(self, a_cyl):
        ...

    # determine if another Sphere intersects this Sphere
    # other is a Sphere object
    # two spheres intersect if they are not strictly inside
    # or not strictly outside each other
    # returns a Boolean
    def does_intersect_sphere(self, other):
        if not self.is_inside_sphere(other):
            dist = self.center.distance(other.center)
            if dist <= self.radius + other.radius:
                return True
        return False

    # determine if a Cube intersects this Sphere
    # the Cube and Sphere intersect if they are not
    # strictly inside or not strictly outside the other
    # a_cube is a Cube object
    # returns a Boolean
    def does_intersect_cube(self, a_cube):
        if not self.is_inside_cube(a_cube):
            for p in a_cube.get_vertices():
                if self.is_inside_point(p):
                    return True
        return False

    # return the largest Cube object that is circumscribed
    # by this Sphere
    # all eight corners of the Cube are on the Sphere
    # returns a Cube object
    def circumscribe_cube(self):
        side = self.radius * 2 / math.sqrt(3)
        c = self.center
        return Cube(c.x, c.y, c.z, side=side)


class Cube (object):
    # Cube is defined by its center (which is a Point object)
    # and side. The faces of the Cube are parallel to x-y, y-z,
    # and x-z planes.
    def __init__(self, x=0, y=0, z=0, side=1):
        self.center = Point(x, y, z)
        self.side = side

    # string representation of a Cube of the form:
    # Center: (x, y, z), Side: value
    def __str__(self):
        p = self.center
        return f'Center: ({p.x}, {p.y}, {p.z}), Side: {self.side}'
    
    # compute the total surface area of Cube (all 6 sides)
    # returns a floating point number
    def area(self):
        return 6 * self.side ** 2

    # compute volume of a Cube
    # returns a floating point number
    def volume(self):
        return self.side ** 3

    # determines if a Point is strictly inside this Cube
    # p is a point object
    # returns a Boolean
    def is_inside_point(self, p):
        min_x, min_y, min_z = math.inf, math.inf, math.inf
        max_x, max_y, max_z = -math.inf, -math.inf, -math.inf

        for ver in self.get_vertices():
            min_x = min(min_x, ver.x)
            min_y = min(min_y, ver.y)
            min_z = min(min_z, ver.z)
            max_x = max(max_x, ver.x)
            max_y = max(max_y, ver.y)
            max_z = max(max_z, ver.z)
        
        return min_x <= p.x <= max_x and min_y <= p.y <= max_y and min_z <= p.z <= max_z

    # determine if a Sphere is strictly inside this Cube
    # a_sphere is a Sphere object
    # returns a Boolean
    def is_inside_sphere(self, a_sphere):
        ...

        
    # determine if another Cube is strictly inside this Cube
    # other is a Cube object
    # returns a Boolean
    def is_inside_cube(self, other):
        for p in other.get_vertices():
            if not self.is_inside_point(p):
                return False
        return True

    # determine if a Cylinder is strictly inside this Cube
    # a_cyl is a Cylinder object
    # returns a Boolean
    def is_inside_cylinder(self, a_cyl):


    # determine if another Cube intersects this Cube
    # two Cube objects intersect if they are not strictly
    # inside and not strictly outside each other
    # other is a Cube object
    # returns a Boolean
    def does_intersect_cube(self, other):
        ...
    # determine the volume of intersection if this Cube
    # intersects with another Cube
    # other is a Cube object
    # returns a floating point number
    def intersection_volume(self, other):
        ...

    # return the largest Sphere object that is inscribed
    # by this Cube
    # Sphere object is inside the Cube and the faces of the
    # Cube are tangential planes of the Sphere
    # returns a Sphere object
    def inscribe_sphere(self):
        diag = self.side * math.sqrt(3)
        return Sphere(self.center.x, self.center.y, self.cetner.z, diag / 2)


    def get_vertices(self):
        Xc, Yc, Zc, SL = self.center.x, self.center.y, self.center.x, self.side
        return [
            Point(Xc + SL/2, Yc + SL/2, Zc + SL/2),
            Point(Xc + SL/2, Yc + SL/2, Zc - SL/2),
            Point(Xc + SL/2, Yc - SL/2, Zc + SL/2),
            Point(Xc + SL/2, Yc - SL/2, Zc - SL/2),
            Point(Xc - SL/2, Yc + SL/2, Zc + SL/2),
            Point(Xc - SL/2, Yc + SL/2, Zc - SL/2),
            Point(Xc - SL/2, Yc - SL/2, Zc + SL/2),
            Point(Xc - SL/2, Yc - SL/2, Zc - SL/2)
        ]


class Cylinder (object):
    # Cylinder is defined by its center (which is a Point object),
    # radius and height. The main axis of the Cylinder is along the
    # z-axis and height is measured along this axis
    def __init__(self, x=0, y=0, z=0, radius=1, height=1):
        self.center = Point(x, y, z)
        self.radius = radius
        self.height = height

    # returns a string representation of a Cylinder of the form:
    # Center: (x, y, z), Radius: value, Height: value
    def __str__(self):
        p = self.center
        return f'Center: ({p.x}, {p.y}, {p.z}), Radius: {self.radius}, Height: {self.height}'

    # compute surface area of Cylinder
    # returns a floating point number
    def area(self):
        return (2 * math.pi * self.radius * self.height) + (2 * math.pi * self.radius ** 2)

    # compute volume of a Cylinder
    # returns a floating point number
    def volume(self):
        return self.height * math.pi * self.radius ** 2

    # determine if a Point is strictly inside this Cylinder
    # p is a Point object
    # returns a Boolean
    def is_inside_point(self, p):
        upper_bound = self.center.z + self.height / 2
        lower_bound = self.center.z - self.height / 2

        p1 = Point(self.center.x, self.center.y)
        p2 = Point(p.x, p.y)

        dist = p1.distance(p2)

        if lower_bound <= p.z <= upper_bound and dist <= self.radius:
            return True
        return False

    # determine if a Sphere is strictly inside this Cylinder
    # a_sphere is a Sphere object
    # returns a Boolean
    def is_inside_sphere(self, a_sphere):

    # determine if a Cube is strictly inside this Cylinder
    # determine if all eight corners of the Cube are inside
    # the Cylinder
    # a_cube is a Cube object
    # returns a Boolean
    def is_inside_cube(self, a_cube):

    # determine if another Cylinder is strictly inside this Cylinder
    # other is Cylinder object
    # returns a Boolean
    def is_inside_cylinder(self, other):

    # determine if another Cylinder intersects this Cylinder
    # two Cylinder object intersect if they are not strictly
    # inside and not strictly outside each other
    # other is a Cylinder object
    # returns a Boolean
    def does_intersect_cylinder(self, other):


def main():
    # read data from standard input

    # read the coordinates of the first Point p

    # create a Point object

    # read the coordinates of the second Point q

    # create a Point object

    # read the coordinates of the center and radius of sphereA

    # create a Sphere object

    # read the coordinates of the center and radius of sphereB

    # create a Sphere object

    # read the coordinates of the center and side of cubeA

    # create a Cube object

    # read the coordinates of the center and side of cubeB

    # create a Cube object

    # read the coordinates of the center, radius and height of cylA

    # create a Cylinder object

    # read the coordinates of the center, radius and height of cylB

    # create a Cylinder object

    # print if the distance of p from the origin is greater
    # than the distance of q from the origin

    # print if Point p is inside sphereA

    # print if sphereB is inside sphereA

    # print if cubeA is inside sphereA

    # print if cylA is inside sphereA

    # print if sphereA intersects with sphereB

    # print if cubeB intersects with sphereB

    # print if the volume of the largest Cube that is circumscribed
    # by sphereA is greater than the volume of cylA

    # print if Point p is inside cubeA

    # print if sphereA is inside cubeA

    # print if cubeB is inside cubeA

    # print if cylA is inside cubeA

    # print if cubeA intersects with cubeB

    # print if the intersection volume of cubeA and cubeB
    # is greater than the volume of sphereA

    # print if the surface area of the largest Sphere object inscribed
    # by cubeA is greater than the surface area of cylA

    # print if Point p is inside cylA

    # print if sphereA is inside cylA

    # print if cubeA is inside cylA

    # print if cylB is inside cylA

    # print if cylB intersects with cylA


if __name__ == "__main__":
    main()
