# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_weakset.py
# case: TestWeakSet_test_contains

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for c in self.letters:
        self.assertEqual(c in self.s, c in self.d)
    self.assertNotIn(1, self.s)
    self.assertIn(self.obj, self.fs)
    del self.obj
    support.gc_collect()
    self.assertNotIn(ustr('F'), self.fs)
