# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_functools.py
# case: TestPartialMethod_test_overriding_keywords

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertEqual(self.a.keywords(a=3), ((self.a,), {'a': 3}))
    self.assertEqual(self.A.keywords(self.a, a=3), ((self.a,), {'a': 3}))
