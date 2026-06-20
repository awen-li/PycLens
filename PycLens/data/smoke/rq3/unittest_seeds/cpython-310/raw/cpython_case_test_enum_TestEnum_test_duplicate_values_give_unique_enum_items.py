# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_enum.py
# case: TestEnum_test_duplicate_values_give_unique_enum_items

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class AutoNumber(Enum):
        first = ()
        second = ()
        third = ()

        def __new__(cls):
            value = len(cls.__members__) + 1
            obj = object.__new__(cls)
            obj._value_ = value
            return obj

        def __int__(self):
            return int(self._value_)
    self.assertEqual(list(AutoNumber), [AutoNumber.first, AutoNumber.second, AutoNumber.third])
    self.assertEqual(int(AutoNumber.second), 2)
    self.assertEqual(AutoNumber.third.value, 3)
    self.assertIs(AutoNumber(1), AutoNumber.first)
