# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_functools.py
# case: TestCmpToKey_test_cmp_to_key

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def cmp1(x, y):
        return (x > y) - (x < y)
    key = self.cmp_to_key(cmp1)
    self.assertEqual(key(3), key(3))
    self.assertGreater(key(3), key(1))
    self.assertGreaterEqual(key(3), key(3))

    def cmp2(x, y):
        return int(x) - int(y)
    key = self.cmp_to_key(cmp2)
    self.assertEqual(key(4.0), key('4'))
    self.assertLess(key(2), key('35'))
    self.assertLessEqual(key(2), key('35'))
    self.assertNotEqual(key(2), key('35'))
