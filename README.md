# Console Engine

Простейший движок, оперирующий **ASCII** графикой для рисования в **консоли**.

## Общая информация

Проект оформлен как пакет.

Обновление картинки происходит раз в секунду.

## Использование

### Инициализация сцены

Так как это пакет, то можно просто импортировать графические объекты из неё.

### Управление

w, a, s, d.

## Пример использования

```python:example/example.py
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

```

Результат:
![example.png](example/example.png)

## Используемые библиотеки

+ math
+ numpy
+ abc (abstract method)
+ sys
+ keyboard
+ pyautogui
+ configparser
