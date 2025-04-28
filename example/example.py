"""
Рабочее пространство
"""
from Engine import Point, Vector, Map, Camera, Console, Plane, BoundedPlane, Sphere, Cube, launch


cam = Camera(Point(-5, 0, 0), Vector(1, 0, 0), 90, 20)

map1 = Map()

map1.append(BoundedPlane(Point(0, 0.3, -2), Vector(0, 1, -1), 1, 2))
map1.append(BoundedPlane(Point(0, 0.3, 2), Vector(0, 1, 1), 1, 2))
map1.append(BoundedPlane(Point(0, -1, 0), Vector(1, 1000000, 0), 2.5, 1))
map1.append(Cube(Point(0, 0, 0), Vector(1, 0, 1), 1))

cons = Console(map1, cam)

launch(cons)
