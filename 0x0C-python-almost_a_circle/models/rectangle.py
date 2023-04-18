#!/usr/bin/python3


"""This module creates a rectangle
It inherits from the ``Base`` class in base.py
"""


from models.base import Base


class Rectangle(Base):
    """Defines Rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializes an instance of a rectangle"""

        Rectangle.validate_attr(width, "width")
        Rectangle.validate_attr(height, "height")
        Rectangle.validate_attr(x, "x")
        Rectangle.validate_attr(y, "y")

        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    def validate_attr(value, name):
        """Validates Attributes"""

        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if name == "width" or name == "height":
            if value <= 0:
                raise ValueError("{} must be > 0".format(name))
        if name == "x" or name == "y":
            if value < 0:
                raise ValueError("{} must be >= 0".format(name))

    @property
    def width(self):
        """Getter for Width"""

        return self.__width

    @width.setter
    def width(self, value):
        """Setter for Width"""
        Rectangle.validate_attr(value, "width")

        self.__width = value

    @property
    def height(self):
        """Getter for Height"""

        return self.__height

    @height.setter
    def height(self, value):
        """Setter for height"""
        Rectangle.validate_attr(value, "height")

        self.__height = value

    @property
    def x(self):
        """Getter for x"""

        return self.__x

    @x.setter
    def x(self, value):
        """Setter for x"""
        Rectangle.validate_attr(value, "x")

        self.__x = value

    @property
    def y(self):
        """Getter for y"""

        return self.__y

    @y.setter
    def y(self, value):
        """Setter for Y"""
        Rectangle.validate_attr(value, "y")

        self.__y = value

    def area(self):
        """Returns the area of rectangle instance"""
        return self.__width * self.__height

    def display(self):
        """Prints the rectangle instace"""
        for y in range(self.y):
            print()
        for i in range(self.height):
            for x in range(self.x):
                print(" ", end="")
            print("#" * self.width)
            if i == self.height:
                print()

    def __str__(self):
        str1 = "[Rectangle] ({}) {}/".format(self.id, self.x)
        str2 = "{} - {}/{}".format(self.y, self.width, self.height)
        return (str1 + str2)

    def update(self, *args, **kwargs):
        """Variable length argument"""

        if len(args) == 0:
            for key, value in kwargs.items():
                setattr(self, key, value)
            return
        i = 0
        attr = ("id", "width", "height", "x", "y")
        for arg in args:
            setattr(self, attr[i], arg)
            i += 1

    def to_dictionary(self):
        """to dictionary conversion"""
        dct = {
                "id": self.id,
                "width": self.width,
                "height": self.height,
                "x": self.x,
                "y": self.y}
        return dct
