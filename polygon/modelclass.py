import inspect
from dataclasses import dataclass


def modelclass(cls):
    cls = dataclass(cls)
    attributes = [
        a
        for a in cls.__dict__["__annotations__"].keys()
        if not a.startswith("__") and not inspect.isroutine(a)
    ]

    def init(self, *args, **kwargs):
        for (i, a) in enumerate(args):
            if i < len(attributes):
                self.__dict__[attributes[i]] = a
        for (k, v) in kwargs.items():
            if k in attributes:
                self.__dict__[k] = v

    cls.__init__ = init

    return cls
