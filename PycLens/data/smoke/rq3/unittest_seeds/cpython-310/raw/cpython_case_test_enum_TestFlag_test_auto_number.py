# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_enum.py
# case: TestFlag_test_auto_number

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class Color(Flag):
        red = auto()
        blue = auto()
        green = auto()
    self.assertEqual(list(Color), [Color.red, Color.blue, Color.green])
    self.assertEqual(Color.red.value, 1)
    self.assertEqual(Color.blue.value, 2)
    self.assertEqual(Color.green.value, 4)
