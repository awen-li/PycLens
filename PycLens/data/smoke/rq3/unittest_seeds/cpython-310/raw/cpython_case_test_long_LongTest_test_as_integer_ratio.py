# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_long.py
# case: LongTest_test_as_integer_ratio

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class myint(int):
        pass
    tests = [10, 0, -10, 1, sys.maxsize + 1, True, False, myint(42)]
    for value in tests:
        (numerator, denominator) = value.as_integer_ratio()
        self.assertEqual((numerator, denominator), (int(value), 1))
        self.assertEqual(type(numerator), int)
        self.assertEqual(type(denominator), int)
