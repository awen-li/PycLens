# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_enum.py
# case: TestEnum_test_no_such_enum_member

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class Color(Enum):
        red = 1
        green = 2
        blue = 3
    with self.assertRaises(ValueError):
        Color(4)
    with self.assertRaises(KeyError):
        Color['chartreuse']
