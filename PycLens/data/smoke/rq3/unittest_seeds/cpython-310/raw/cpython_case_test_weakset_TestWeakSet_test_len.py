# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_weakset.py
# case: TestWeakSet_test_len

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertEqual(len(self.s), len(self.d))
    self.assertEqual(len(self.fs), 1)
    del self.obj
    support.gc_collect()
    self.assertEqual(len(self.fs), 0)
