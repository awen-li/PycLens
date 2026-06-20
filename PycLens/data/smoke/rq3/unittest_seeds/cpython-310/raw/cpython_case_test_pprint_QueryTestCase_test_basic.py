# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_pprint.py
# case: QueryTestCase_test_basic

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    pp = pprint.PrettyPrinter()
    for safe in (2, 2.0, 2j, 'abc', [3], (2, 2), {3: 3}, b'def', bytearray(b'ghi'), True, False, None, ..., self.a, self.b):
        self.assertFalse(pprint.isrecursive(safe), 'expected not isrecursive for %r' % (safe,))
        self.assertTrue(pprint.isreadable(safe), 'expected isreadable for %r' % (safe,))
        self.assertFalse(pp.isrecursive(safe), 'expected not isrecursive for %r' % (safe,))
        self.assertTrue(pp.isreadable(safe), 'expected isreadable for %r' % (safe,))
