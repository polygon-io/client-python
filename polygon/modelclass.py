import inspect
import typing
from dataclasses import dataclass


_T = typing.TypeVar("_T")


def modelclass(cls: typing.Type[_T]) -> typing.Type[_T]:
    cls = dataclass(cls)
    attributes = [
        a
        for a in cls.__dict__["__annotations__"].keys()
        if not a.startswith("__") and not inspect.isroutine(a)
    ]

    def init(self, *args, **kwargs):
        for i, a in enumerate(args):
            if i < len(attributes):
                self.__dict__[attributes[i]] = a
        for k, v in kwargs.items():
            if k in attributes:
                self.__dict__[k] = v

    cls.__init__ = init  # type: ignore[assignment]

    return cls
