from abc import abstractmethod, ABC


class Shape(ABC):

    def __init__(self, color):
        self._color = color

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def scale(self, ratio):
        pass


class Rectangle(Shape):
    def __init__(self, width, height, color):
        Shape.__init__(self, color)
        self._width = width
        self._height = height

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, height):
        self._height = height

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, width):
        self._width = width

    def area(self):
        return self._height * self._width

    def scale(self, ratio):
        self._width *= ratio
        self._height *= ratio

    def __str__(self):
        return ("I'm a Rectangle!")


class Circle(Shape):

    def __init__(self, radius, color):
        Shape.__init__(self, color)
        self._radius = radius

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, radius):

        self._radius = radius

    def area(self):
        return 3.14 * self._radius * self._radius

    def scale(self, ratio):
        self._radius *= ratio

    def __str__(self):
        return ("I'm a Circle!")
