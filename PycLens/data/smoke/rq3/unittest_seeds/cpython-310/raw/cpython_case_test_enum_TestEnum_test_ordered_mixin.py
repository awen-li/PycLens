# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_enum.py
# case: TestEnum_test_ordered_mixin

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class OrderedEnum(Enum):

        def __ge__(self, other):
            if self.__class__ is other.__class__:
                return self._value_ >= other._value_
            return NotImplemented

        def __gt__(self, other):
            if self.__class__ is other.__class__:
                return self._value_ > other._value_
            return NotImplemented

        def __le__(self, other):
            if self.__class__ is other.__class__:
                return self._value_ <= other._value_
            return NotImplemented

        def __lt__(self, other):
            if self.__class__ is other.__class__:
                return self._value_ < other._value_
            return NotImplemented

    class Grade(OrderedEnum):
        A = 5
        B = 4
        C = 3
        D = 2
        F = 1
    self.assertGreater(Grade.A, Grade.B)
    self.assertLessEqual(Grade.F, Grade.C)
    self.assertLess(Grade.D, Grade.A)
    self.assertGreaterEqual(Grade.B, Grade.B)
    self.assertEqual(Grade.B, Grade.B)
    self.assertNotEqual(Grade.C, Grade.D)
