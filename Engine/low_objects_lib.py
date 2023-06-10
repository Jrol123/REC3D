"""
Эта библиотека содержит в себе реализацию низкоуровневых объектов для движка.

Notes:
    + Для упрощения работы, VectorSpace может быть получен через Vector.
    + Существуют лишь радиус-векторы.
    + При изменении базиса векторы не перестраиваются.
    + Можно попробовать добавить 4-е измерение.

Attributes
---------
engine_config : cfg
    Конфиг с параметрами VectorSpace.

    Attributes:
        init_point
            Координаты начальной точки в формате (x, y, z).

        basis
            Координаты базисных векторов в формате (x, y, z).

Classes
-------
Point
    Точка.

Vector
    Вектор.

VectorSpace
    Пространство, относительно которого будет всё строиться. \n
    Базис и начальная точка берутся из конфига

Map
    Множество объектов.

Ray
    Луч.

"""

import math
import configparser


class Point:
    """
    Класс для представления точки в трехмерном пространстве.

    :ivar coords: Координаты точки.
    :type coords: list[float].

    :param obj: Список координат точки в формате (x, y, z).
    :type obj: tuple[float]

    :raise AttributeError: Если были введены не 3 координаты.

    """

    def __init__(self, *obj: float):
        """
        Инициализация класса

        :param obj: Список координат точки в формате (x, y, z).
        :type obj: tuple[float]

        :raise AttributeError: Если были введены не 3 координаты

        """
        if len(obj) == 3 and all(isinstance(obj[i], (int, float)) for i in range(0, 2 + 1)):
            self.coords = list(obj)
        else:
            raise AttributeError("Необходимо передавать 3 координаты в формате (x, y, z).")

    def __str__(self):
        return "Point({:.4f}, {:.4f}, {:.4f})".format(*self.coords)

    def __bool__(self):
        return bool(sum(self.coords))

    def __eq__(self, other):
        return self.coords == other.coords

    def __ne__(self, other):
        return self.coords != other.coords

    def __add__(self, other):
        return Point(*[self.coords[i] + other.coords[i]
                       for i in range(3)])

    def __mul__(self, other):
        assert isinstance(other, (int, float))

        return Point(*[self.coords[i] * other
                       for i in range(3)])

    def __sub__(self, other):
        return self.__add__(-1 * other)

    def __rmul__(self, other):
        return self.__mul__(other)

    def __truediv__(self, other: [int, float]):
        assert other != 0
        return self.__mul__(1 / other)

    def distance(self, other) -> float:
        """
        Дистанция между двумя точками
        
        :param other: Другая точка
        :type other: Point
        :return: Дистанция между двумя точками
        :rtype: float
        
        """

        return math.sqrt(sum((self.coords[i] - other.coords[i]) ** 2 for i in range(3)))


class Vector:
    """
    Класс для представления радиус-вектора в трехмерном пространстве.

    Начальная точка равна начальной точке VectorSpace. Конечная точка задаётся.

    :ivar point: Точка радиус-вектора.
    :type point: Point

    :param args: Список координат точки вектора в формате (x, y, z) ИЛИ в формате (Point).
    :type args: tuple[float], tuple[Point]

    :raise AttributeError: Если было передано неправильное количество аргументов

    """

    # vs = VectorSpace()
    def __init__(self, *args: [float | Point]):
        """
        Инициализация класса

        :param args: Список координат точки вектора в формате (x, y, z) ИЛИ в формате (Point).
        :type args: float | Point

        :raise AttributeError: Если было передано неправильное количество аргументов.

        """
        if len(args) == 1:
            assert isinstance(args[0], Point)
            self.point = args[0]  # Point(x, y, z)
        elif len(args) == 3:
            assert all(map(isinstance, args, [(int, float)] * 3))
            self.point = Point(*args)
        else:
            raise AttributeError("Необходимо передавать координаты точки радиус вектора в формате (x, y, z) "
                                 "ИЛИ в формате (Point).")

        # self.vs = vs

    def __str__(self):
        return "Vector({:.4f}, {:.4f}, {:.4f})".format(
            *self.point.coords)

    def len(self) -> float:
        """
        Вычисление длины вектора.

        :return: Длина вектора.
        :rtype: float

        """
        return self.vs.init_pt.distance(self.point)

    def normalize(self):
        """
        Нормализация длины вектора

        Происходит с помощью деления координат вектора на его длину.

        :return: Нормализованный вектор
        :rtype: Vector

        """
        if self.len() == 0:
            return self

        return Vector(self.point / self.len())

    def __bool__(self):
        return bool(self.point)

    def __eq__(self, other: "Vector"):
        return self.point == other.point

    def __ne__(self, other: "Vector"):
        return self.point != other.point

    def __add__(self, other: "Vector"):
        return Vector(self.point + other.point)

    def __sub__(self, other):
        return Vector(self.point - other.point)

    def __mul__(self, other):
        """
        Скалярное произведение векторов.

        Также является произведением на число.

        :param other: Другой вектор.
        :type other: Vector | float

        :return: Скаляр, если other — Vector | Vector, если other — float.
        :rtype: Vector | float

        """
        if isinstance(other, Vector):
            return sum(self.point.coords[i] * other.point.coords[i]
                       for i in range(3))
        else:
            return Vector(self.point * other)

    def __rmul__(self, other):
        assert isinstance(other, (int, float))

        return Vector(self.point * other)

    def __truediv__(self, other):
        assert isinstance(other, (int, float))

        return Vector(self.point / other)

    def __pow__(self, other):
        """
        Векторное произведение.

        :param other: Другой вектор.
        :type other: Vector
        :return: Вектор, являющийся результатом векторного произведения.
        :rtype: Vector

        """
        x1 = self.point.coords[0]
        y1 = self.point.coords[1]
        z1 = self.point.coords[2]
        x2 = other.point.coords[0]
        y2 = other.point.coords[1]
        z2 = other.point.coords[2]

        x = self.vs.basis[0] * (y1 * z2 - y2 * z1)
        y = self.vs.basis[1] * -(x1 * z2 - x2 * z1)
        z = self.vs.basis[2] * (y2 * x1 - y1 * x2)

        return x + y + z

    def rotate(self, x_angle: float = 0, y_angle: float = 0,
               z_angle: float = 0):
        """
        Поворот по всем осям.

        Реализован через повороты Эйлера. \n
        Так, x_angle — поворот в плоскости YZ и т. д.

        :param x_angle: Угол крена.
        :type x_angle: float
        :param y_angle: Угол тангажа.
        :type y_angle: float
        :param z_angle: Угол рысканья.
        :type z_angle: float

        :return: Изменяет сам вектор.
        :rtype: None

        """
        # issue 1

        x_angle = math.pi * x_angle / 360
        y_angle = math.pi * y_angle / 360
        z_angle = math.pi * z_angle / 360

        # Поворот вокруг оси Ox
        y_old = self.point.coords[1]
        z_old = self.point.coords[2]
        self.point.coords[1] = y_old * math.cos(x_angle) \
                               - z_old * math.sin(x_angle)
        self.point.coords[2] = y_old * math.sin(x_angle) \
                               + z_old * math.cos(x_angle)

        # Поворот вокруг оси Oy
        x_old = self.point.coords[0]
        z_old = self.point.coords[2]
        self.point.coords[0] = x_old * math.cos(y_angle) \
                               + z_old * math.sin(y_angle)
        self.point.coords[2] = x_old * -math.sin(y_angle) \
                               + z_old * math.cos(y_angle)

        # Поворот вокруг оси Oz
        x_old = self.point.coords[0]
        y_old = self.point.coords[1]
        self.point.coords[0] = x_old * math.cos(z_angle) \
                               - y_old * math.sin(z_angle)
        self.point.coords[1] = x_old * math.sin(z_angle) \
                               + y_old * math.cos(z_angle)


class VectorSpace:
    """
    Класс для представления векторного пространства.

    Реализован для трёх измерений. \n
    Начальные данные берутся из конфига.

    :ivar init_pt: Точка начала координат.
    :type init_pt: Point
    :ivar basis: Базис векторного пространства.
    :type basis: list[Vector, Vector, Vector]

    :param init_pt: Точка начала координат.
    :type init_pt: Point
    :param direct_args: Список векторов базиса векторного пространства.
    :type direct_args: Vector

    :raise AttributeError: Если было введено не 3 вектора для направлений.

    """
    # issue 2

    # init_pt = Point(0, 0, 0)
    # basis = [Vector(1, 0, 0), Vector(0, 1, 0), Vector(0, 0, 1)]

    config = configparser.ConfigParser()
    config.read("engine_config.cfg")

    t = str(config['SPACE']['init_point'])
    init_pt = Point(*(float(x) for x in (t.split(','))))

    t = str(config['SPACE']['basis'])
    basis = []
    for st in t.split('|'):
        basis.append(Vector(*(float(x) for x in (st.split(',')))))

    def __init__(self, init_pt: Point, *direct_args: Vector):
        """
        Ручная инициализация класса.

        Используется, если нужно переделать VectorSpace после его начальной инициализации через конфиг.

        :param init_pt: Точка начала координат.
        :type init_pt: Point
        :param direct_args: Список векторов базиса векторного пространства.
        :type direct_args: Vector

        :raise AttributeError: Если было введено не 3 вектора для направлений.

        """
        self.init_pt = init_pt

        if len(direct_args) == 3:
            self.basis = list(direct_args)
        else:
            raise AttributeError("Необходимо передавать 3 вектора для направлений.")


# Vector.vs = VectorSpace()


class Map:
    """
    Класс для списка объектов.

    Используется для отрисовки объектов.

    :ivar _obj_list: Список объектов.
    :type _obj_list: Object

    :param args: Множество объектов.
    :type args: Object | None

    """
    _obj_list = []

    def __init__(self, *args):
        """
        Инициализация класса.

        :param args: Множество объектов.
        :type args: Object | None

        """
        self._obj_list = [*args]

    def append(self, *objs) -> None:
        """
        Добавление объектов в список.

        :param objs: Список объектов.
        :type objs: Object

        :return: Добавляет в самого себя объект.
        :rtype: None

        """
        self._obj_list.extend(objs)

    def __getitem__(self, item):
        return self._obj_list[item]

    def __iter__(self):
        return iter(self._obj_list)


class Ray:
    """
    Класс для Луча.

    :ivar inpt: Начальная точка.
    :type inpt: Point
    :ivar dir: Направление луча.
    :type dir: Vector

    :param ipt: Начальная точка.
    :type ipt: Point
    :param direction: Направление луча.
    :type direction: Vector

    """

    def __init__(self, ipt: Point, direction: Vector):
        """
        Инициализация класса.

        :param ipt: Начальная точка.
        :type ipt: Point
        :param direction: Направление луча.
        :type direction: Vector

        """
        self.inpt = ipt
        self.dir = direction

    def __str__(self):
        return f"Ray({self.inpt}, {self.dir})"

    def intersect(self, mapping: Map) -> list[float]:
        """
        Определение пересечения луча с объектами.

        Работает перебором всех объектов.

        :param mapping: Список объектов.
        :type mapping: Map
        :return: Расстояние до каждого из объектов.
        :rtype: list[float]

        """
        return [obj.intersect(self) for obj in mapping]
