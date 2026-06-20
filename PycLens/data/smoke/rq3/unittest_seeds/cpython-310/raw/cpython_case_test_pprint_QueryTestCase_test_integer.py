# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_pprint.py
# case: QueryTestCase_test_integer

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertEqual(pprint.pformat(1234567), '1234567')
    self.assertEqual(pprint.pformat(1234567, underscore_numbers=True), '1_234_567')

    class Temperature(int):

        def __new__(cls, celsius_degrees):
            return super().__new__(Temperature, celsius_degrees)

        def __repr__(self):
            kelvin_degrees = self + 273.15
            return f'{kelvin_degrees}°K'
    self.assertEqual(pprint.pformat(Temperature(1000)), '1273.15°K')
