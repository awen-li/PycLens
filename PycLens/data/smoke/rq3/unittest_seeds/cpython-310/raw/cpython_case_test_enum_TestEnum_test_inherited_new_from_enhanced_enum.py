# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_enum.py
# case: TestEnum_test_inherited_new_from_enhanced_enum

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class AutoNumber(Enum):

        def __new__(cls):
            value = len(cls.__members__) + 1
            obj = object.__new__(cls)
            obj._value_ = value
            return obj

        def __int__(self):
            return int(self._value_)

    class Color(AutoNumber):
        red = ()
        green = ()
        blue = ()
    self.assertEqual(list(Color), [Color.red, Color.green, Color.blue])
    self.assertEqual(list(map(int, Color)), [1, 2, 3])
