#!/usr/bin/python3

"""Square Class child of Rectangle"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Squaer class"""

    def __init__(self, size, x=0, y=0, id=None):
        """constructor of square class"""

        super().__init__(size, size, x, y, id)

    def __str__(self):
        str1 = "[Square] ({}) {}/".format(self.id, self.x)
        str2 = "{} - {}".format(self.y, self.width)
        return (str1 + str2)

    @property
    def size(self):
        """Getter for size"""
        return self.width

    @size.setter
    def size(self, value):
        """setter for size"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Variable length argument"""

        if len(args) == 0:
            for key, value in kwargs.items():
                setattr(self, key, value)
            return
        i = 0
        attr = ("id", "size", "x", "y")
        for arg in args:
            setattr(self, attr[i], arg)
            i += 1

    def to_dictionary(self):
        """to dictionary conversion"""
        dct = {
                "id": self.id,
                "size": self.width,
                "x": self.x,
                "y": self.y}
        return dct
