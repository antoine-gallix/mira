from icecream import ic
from functools import wraps


# -------------------core----------------------------
class Sieve:
    def __init__(self, function, repr=None):
        self._sieve = function
        if repr is not None:
            self._repr = repr
        else:
            self._repr = function.__name__

    def __call__(self, thing):
        return self._sieve(thing)

    def __repr__(self):
        return f"{self.__class__.__name__}({self._repr})"

    @classmethod
    def _ensure_sieve(cls, func_of_sieve):
        if not isinstance(func_of_sieve, cls):
            return cls(func_of_sieve)
        else:
            return func_of_sieve

    def __and__(self, sieve):
        sieve = self._ensure_sieve(sieve)

        def intersection(x):
            return self._sieve(x) and sieve(x)

        return self.__class__(intersection, repr=f"{self._repr} & {sieve._repr}")

    def __or__(self, sieve):
        sieve = self._ensure_sieve(sieve)

        def union(x):
            return self._sieve(x) or sieve(x)

        return self.__class__(union, repr=f"{self._repr} | {sieve._repr}")

    def _not(self):
        def negated(x):
            return not (self._sieve(x))

        return self.__class__(negated, f"not({self._repr})")


def sieve(func):
    """Decorator to change functions into sieves"""

    return Sieve(func)


# -----------------------utils------------------------


null_sieve = Sieve(lambda _: True, "True")


def is_instance(type_):
    """Factory of filters based on class/type"""

    def filter_(thing):
        return isinstance(thing, type_)

    return Sieve(filter_, f"is_instance({type_.__name__})")
