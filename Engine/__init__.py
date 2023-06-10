"""
Этот пакет позволяет создавать простейшую графику в консоли в 3-х мерном пространстве.

Список зависимостей:
    math
    numpy
    abc (abstract method)
    sys
    keyboard
    pyautogui
    configparser

Artemii Popovkin [https://github.com/Jrol123/REC3D]
angap4@gmail.com

# License: MIT

"""

from Engine.low_objects_lib import Point, Vector, VectorSpace, Ray, Map
from Engine.high_objects_lib import Plane, BoundedPlane, Cube, Sphere
from Engine.vision_lib import Camera, Console
from Engine.action_lib import launch

__author__ = 'Artemii Popovkin'

__version__ = "0.9.4"
