from datetime import datetime
import random


@property
def simple_func(var: int, var2: int = 6) -> int:
    ans = var + var2
    return ans


class SimpleClass:
    somevar = ""
    another: int = 8
    aaaaanother: dict

    def __str__(self) -> str:
        """ """

    # a comment

    def __init__(self):
        self.num = 9

    def zefunc(self):
        """ """
        # another comment
        a = 5

    def another(self):
        """ """

    # Seat
    @property
    def zippe(self) -> str:
        """ """

    @property
    def num(self) -> int:
        """This class's number."""
        return self._num

    @num.setter
    def num(self, new_val: int):
        self._num = new_val

    another = ""
    # Seat
    something = ""
    double = ""

    def __yeet__(self):
        """ """


class AnotherClass:
    def some_func(self):
        # comment
        return ""
