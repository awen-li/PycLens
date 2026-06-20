# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_enum.py
# case: TestEnum_test_auto_garbage_corrected

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class Color(Enum):
        red = 'red'
        blue = 2
        green = auto()
    self.assertEqual(list(Color), [Color.red, Color.blue, Color.green])
    self.assertEqual(Color.red.value, 'red')
    self.assertEqual(Color.blue.value, 2)
    self.assertEqual(Color.green.value, 3)
