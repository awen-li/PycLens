# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_pprint.py
# case: QueryTestCase_test_knotted

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.b[67] = self.a
    self.d = {}
    self.d[0] = self.d[1] = self.d[2] = self.d
    pp = pprint.PrettyPrinter()
    for icky in (self.a, self.b, self.d, (self.d, self.d)):
        self.assertTrue(pprint.isrecursive(icky), 'expected isrecursive')
        self.assertFalse(pprint.isreadable(icky), 'expected not isreadable')
        self.assertTrue(pp.isrecursive(icky), 'expected isrecursive')
        self.assertFalse(pp.isreadable(icky), 'expected not isreadable')
    self.d.clear()
    del self.a[:]
    del self.b[:]
    for safe in (self.a, self.b, self.d, (self.d, self.d)):
        self.assertFalse(pprint.isrecursive(safe), 'expected not isrecursive for %r' % (safe,))
        self.assertTrue(pprint.isreadable(safe), 'expected isreadable for %r' % (safe,))
        self.assertFalse(pp.isrecursive(safe), 'expected not isrecursive for %r' % (safe,))
        self.assertTrue(pp.isreadable(safe), 'expected isreadable for %r' % (safe,))
