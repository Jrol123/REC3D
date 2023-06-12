"""
Рабочее пространство
"""
from Engine import Point, Vector, Map, Camera, Console, Plane, BoundedPlane, Sphere, Cube, launch


cam = Camera(Point(-6, 2, 0), Vector(1, 0, 0), 90, 20)

map1 = Map()

b_place = 4

map1.append(BoundedPlane(Point(10, 3, 0), Vector(1, 0, 0), 1, 3))
map1.append(BoundedPlane(Point(10, 6, 0), Vector(0, 1, 0), 4, 1))

map1.append(Cube(Point(10, 1.5, -b_place), Vector(1, 0, 0), 3))
map1.append(Cube(Point(10, 1.5, b_place), Vector(1, 0, 0), 3))
map1.append(Sphere(Point(9, 4, -b_place), Vector(1, 0, 0), 1))
map1.append(Sphere(Point(9, 4, b_place), Vector(1, 0, 0), 1))

cons = Console(map1, cam)

launch(cons)





