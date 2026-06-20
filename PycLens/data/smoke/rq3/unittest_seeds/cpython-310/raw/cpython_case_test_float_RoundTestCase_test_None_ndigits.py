# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_float.py
# case: RoundTestCase_test_None_ndigits

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for x in (round(1.23), round(1.23, None), round(1.23, ndigits=None)):
        self.assertEqual(x, 1)
        self.assertIsInstance(x, int)
    for x in (round(1.78), round(1.78, None), round(1.78, ndigits=None)):
        self.assertEqual(x, 2)
        self.assertIsInstance(x, int)
