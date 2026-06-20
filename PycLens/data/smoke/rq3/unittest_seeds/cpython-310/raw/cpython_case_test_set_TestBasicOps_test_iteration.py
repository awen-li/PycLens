# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_set.py
# case: TestBasicOps_test_iteration

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for v in self.set:
        self.assertIn(v, self.values)
    setiter = iter(self.set)
    self.assertEqual(setiter.__length_hint__(), len(self.set))
