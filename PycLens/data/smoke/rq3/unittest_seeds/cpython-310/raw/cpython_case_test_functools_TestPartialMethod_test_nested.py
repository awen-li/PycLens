# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_functools.py
# case: TestPartialMethod_test_nested

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertEqual(self.a.nested(), ((self.a, 1, 5), {}))
    self.assertEqual(self.a.nested(6), ((self.a, 1, 5, 6), {}))
    self.assertEqual(self.a.nested(d=7), ((self.a, 1, 5), {'d': 7}))
    self.assertEqual(self.a.nested(6, d=7), ((self.a, 1, 5, 6), {'d': 7}))
    self.assertEqual(self.A.nested(self.a, 6, d=7), ((self.a, 1, 5, 6), {'d': 7}))
