# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_enum.py
# case: TestEnum_test_auto_order_wierd

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    weird_auto = auto()
    weird_auto.value = 'pathological case'

    class Color(Enum):
        red = weird_auto

        def _generate_next_value_(name, start, count, last):
            return name
        blue = auto()
    self.assertEqual(list(Color), [Color.red, Color.blue])
    self.assertEqual(Color.red.value, 'pathological case')
    self.assertEqual(Color.blue.value, 'blue')
