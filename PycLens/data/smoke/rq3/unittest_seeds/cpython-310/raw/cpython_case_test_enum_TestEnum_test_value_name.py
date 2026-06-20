# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_enum.py
# case: TestEnum_test_value_name

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    Season = self.Season
    self.assertEqual(Season.SPRING.name, 'SPRING')
    self.assertEqual(Season.SPRING.value, 1)
    with self.assertRaises(AttributeError):
        Season.SPRING.name = 'invierno'
    with self.assertRaises(AttributeError):
        Season.SPRING.value = 2
