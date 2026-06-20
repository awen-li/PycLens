# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_enum.py
# case: TestEnum_test_no_duplicates

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class UniqueEnum(Enum):

        def __init__(self, *args):
            cls = self.__class__
            if any((self.value == e.value for e in cls)):
                a = self.name
                e = cls(self.value).name
                raise ValueError('aliases not allowed in UniqueEnum:  %r --> %r' % (a, e))

    class Color(UniqueEnum):
        red = 1
        green = 2
        blue = 3
    with self.assertRaises(ValueError):

        class Color(UniqueEnum):
            red = 1
            green = 2
            blue = 3
            grene = 2
