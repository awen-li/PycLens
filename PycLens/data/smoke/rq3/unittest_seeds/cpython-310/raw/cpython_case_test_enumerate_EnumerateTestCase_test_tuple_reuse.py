# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_enumerate.py
# case: EnumerateTestCase_test_tuple_reuse

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertEqual(len(set(map(id, list(enumerate(self.seq))))), len(self.seq))
    self.assertEqual(len(set(map(id, enumerate(self.seq)))), min(1, len(self.seq)))
