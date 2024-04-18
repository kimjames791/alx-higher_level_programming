#!/usr/bin/python3
"""
...
"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """
    ...
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        ...
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
        ...
        """
        return '[Square] ({:d}) {:d}/{:d} - {:d}'.format(
            self.id, self.x, self.y, self.width
        )

    @property
    def size(self):
        """
        ...
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        ...
        """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """
        ...
        """
        argc = len(args)
        kwargc = len(kwargs)
        modif_attrs = ['id', 'size', 'x', 'y']

        if argc > 4:
            argc = 4

        if argc > 0:
            for p in range(argc):
                setattr(self, modif_attrs[p], args[p])
        elif kwargc > 0:
            for g, h in kwargs.items():
                if g in modif_attrs:
                    setattr(self, g, h)

    def to_dictionary(self):
        """
        ...
        """
        return {
            'id': self.id,
            'size': self.size,
            'x': self.x,
            'y': self.y
        }
