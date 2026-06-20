# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_functools.py
# case: TestPartialMethod_test_descriptors

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for obj in [self.A, self.a]:
        with self.subTest(obj=obj):
            self.assertEqual(obj.static(), ((8,), {}))
            self.assertEqual(obj.static(5), ((8, 5), {}))
            self.assertEqual(obj.static(d=8), ((8,), {'d': 8}))
            self.assertEqual(obj.static(5, d=8), ((8, 5), {'d': 8}))
            self.assertEqual(obj.cls(), ((self.A,), {'d': 9}))
            self.assertEqual(obj.cls(5), ((self.A, 5), {'d': 9}))
            self.assertEqual(obj.cls(c=8), ((self.A,), {'c': 8, 'd': 9}))
            self.assertEqual(obj.cls(5, c=8), ((self.A, 5), {'c': 8, 'd': 9}))
