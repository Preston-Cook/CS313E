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
    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return f'({self.x}, {self.y}, {self.z})'

    def distance(self, other):
        x1, y1, z1 = self.x, self.y, self.z
        x2, y2, z2 = other.x, other.y, other.z

        return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y and self.z == other.z


class Sphere (object):
    def __init__(self, x=0, y=0, z=0, radius=1):
        self.x = x
        self.y = y
        self.z = z
        self.radius = radius

    def __str__(self):
        return f'Center: ({self.x}, {self.y}, {self.z}), Radius: {self.radius}'

    def area(self):
        return 4 * math.pi * self.radius ** 2

    def volume(self):
        return (4/3) * math.pi * self.radius ** 3

    def is_inside_point(self, p):
        p1 = Point(self.x, self.y, self.z)
        p2 = p

        dist = p1.distance(p2)

        return dist <= self.radius

    def is_inside_sphere(self, other):
        if self.radius > other.radius:
            lr, sr = self.radius, other.radius
        else:
            lr, sr = other.radius, self.radius

        p1 = Point(self.x, self.y, self.z)
        p2 = Point(other.x, other.y, other.z)

        dist = p1.distance(p2)

        return dist <= lr - sr

    def is_inside_cube(self, a_cube):
        p1 = Point(self.x, self.y, self.z)

        for x, y, z in a_cube.get_vertices():
            p2 = Point(x, y, z)
            if p1.distance(p2) > self.radius:
                return False
        return True

    def is_inside_cyl(self, a_cyl):
        p1 = Point(self.x, self.y, self.z)

        for x, y, z in a_cyl.get_major_points():
            p2 = Point(x, y, z)
            if p1.distance(p2) > self.radius:
                return False
        return True

    def does_intersect_sphere(self, other):
        p1 = Point(self.x, self.y, self.z)
        p2 = Point(other.x, other.y, other.z)

        dist = p1.distance(p2)

        return dist <= self.radius + other.radius

    def does_intersect_cube(self, a_cube):
        if not self.is_inside_cube(a_cube):
            p1 = Point(self.x, self.y, self.z)
            for x, y, z in a_cube.get_vertices():
                p2 = Point(x, y, z)
                if p1.distance(p2) <= self.radius:
                    return True
        return False

    def circumscribe_cube(self):
        diag = self.radius * 2
        side = diag / math.sqrt(3)

        return Cube(self.x, self.y, self.z, side=side)


class Cube (object):

    def __init__(self, x=0, y=0, z=0, side=1):
        self.x = x
        self.y = y
        self.z = z
        self.side = side

    def __str__(self):
        return f'Center: ({self.x}, {self.y}, {self.z}), Side: {self.side}'

    def area(self):
        return 6 * self.side ** 2

    def volume(self):
        return self.side ** 3

    def is_inside_point(self, p):
        min_x, min_y, min_z = math.inf, math.inf, math.inf
        max_x, max_y, max_z = -math.inf, -math.inf, -math.inf
        
        for x, y, z in self.get_vertices():
            min_x = min(min_x, x)
            min_y = min(min_y, y)
            min_z = min(min_z, z)
            max_x = max(max_x, x)
            max_y = max(max_y, y)
            max_z = max(max_z, z)
        
        return min_x <= p.x <= max_x and min_y <= p.y <= max_y and min_z <= p.z <= max_x 

    def is_inside_sphere(self, a_sphere):
        SX, SY, SZ, R = a_sphere.x, a_sphere.y, a_sphere.z, a_sphere.radius

        points = [
            Point(SX, SY, SZ + R),
            Point(SX, SY, SZ - R),
            Point(SX, SY + R, SZ),
            Point(SX, SY - R, SZ),
            Point(SX + R, SY, SZ),
            Point(SX - R, SY, SZ)
        ]
        
        for point in points:
            if not self.is_inside_point(point):
                return False
        return True

    def is_inside_cube(self, other):
        for x, y, z in other.get_vertices():
            p = Point(x, y, z)
            if not self.is_inside_point(p):
                return False
        return True

    def is_inside_cylinder(self, a_cyl):
        p1 = Point(self.x, self.y, self.z)

        for x, y, z in a_cyl.get_major_points():
            p = Point(x, y, z)
            if not self.is_inside_point(p):
                return False
        return True

    def does_intersect_cube(self, other):
        if not self.is_inside_cube(other):
            for x, y, z in other.get_vertices():
                p = Point(x, y, z)
                if self.is_inside_point(p):
                    return True
        return False

    def intersection_volume(self, other):
        ...

    def inscribe_sphere(self):
        diag = self.side * math.sqrt(3)
        return Sphere(self.x, self.y, self.z, diag / 2)

    def get_vertices(self):
        Xc, Yc, Zc, SL = self.x, self.y, self.x, self.side
        return [[Xc + SL/2, Yc + SL/2, Zc + SL/2],
                [Xc + SL/2, Yc + SL/2, Zc - SL/2],
                [Xc + SL/2, Yc - SL/2, Zc + SL/2],
                [Xc + SL/2, Yc - SL/2, Zc - SL/2],
                [Xc - SL/2, Yc + SL/2, Zc + SL/2],
                [Xc - SL/2, Yc + SL/2, Zc - SL/2],
                [Xc - SL/2, Yc - SL/2, Zc + SL/2],
                [Xc - SL/2, Yc - SL/2, Zc - SL/2]] 


class Cylinder (object):

    def __init__(self, x=0, y=0, z=0, radius=1, height=1):
        self.x = x
        self.y = y
        self.z = z
        self.radius = radius
        self.height = height

    def __str__(self):
        return f'Center: ({self.x}, {self.y}, {self.z}), Radius: {self.radius}, Height: {self.height}'

    def area(self):
        return 2 * (math.pi * self.radius * self.height) + 2 * (math.pi * self.radius ** 2)

    def volume(self):
        return math.pi * self.radius ** 2 * self.height

    def is_inside_point(self, p):
        ...

    def is_inside_sphere(self, a_sphere):
        ...

    def is_inside_cube(self, a_cube):
        ...

    def is_inside_cylinder(self, other):
        ...

    def does_intersect_cylinder(self, other):
        ...

    def get_major_points(self):
        HALF_HEIGHT = self.height * 0.5
        return [
            [self.x - self.radius, self.y, self.z - HALF_HEIGHT],
            [self.x + self.radius, self.y, self.z - HALF_HEIGHT],
            [self.x, self.y - self.radius, self.z - HALF_HEIGHT],
            [self.x, self.y + self.radius, self.z - HALF_HEIGHT],
            [self.x + self.radius, self.y, self.z + HALF_HEIGHT],
            [self.x - self.radius, self.y, self.z + HALF_HEIGHT],
            [self.x, self.y - self.radius, self.z + HALF_HEIGHT],
            [self.x, self.y + self.radius, self.z + HALF_HEIGHT]
        ]


# def main():
#     # read data from standard input

#     # read the coordinates of the first Point p

#     # create a Point object

#     # read the coordinates of the second Point q

#     # create a Point object

#     # read the coordinates of the center and radius of sphereA

#     # create a Sphere object

#     # read the coordinates of the center and radius of sphereB

#     # create a Sphere object

#     # read the coordinates of the center and side of cubeA

#     # create a Cube object

#     # read the coordinates of the center and side of cubeB

#     # create a Cube object

#     # read the coordinates of the center, radius and height of cylA

#     # create a Cylinder object

#     # read the coordinates of the center, radius and height of cylB

#     # create a Cylinder object

#     # print if the distance of p from the origin is greater
#     # than the distance of q from the origin

#     # print if Point p is inside sphereA

#     # print if sphereB is inside sphereA

#     # print if cubeA is inside sphereA

#     # print if cylA is inside sphereA

#     # print if sphereA intersects with sphereB

#     # print if cubeB intersects with sphereB

#     # print if the volume of the largest Cube that is circumscribed
#     # by sphereA is greater than the volume of cylA

#     # print if Point p is inside cubeA

#     # print if sphereA is inside cubeA

#     # print if cubeB is inside cubeA

#     # print if cylA is inside cubeA

#     # print if cubeA intersects with cubeB

#     # print if the intersection volume of cubeA and cubeB
#     # is greater than the volume of sphereA

#     # print if the surface area of the largest Sphere object inscribed
#     # by cubeA is greater than the surface area of cylA

#     # print if Point p is inside cylA

#     # print if sphereA is inside cylA

#     # print if cubeA is inside cylA

#     # print if cylB is inside cylA

#     # print if cylB intersects with cylA


# if __name__ == "__main__":
#     main()
