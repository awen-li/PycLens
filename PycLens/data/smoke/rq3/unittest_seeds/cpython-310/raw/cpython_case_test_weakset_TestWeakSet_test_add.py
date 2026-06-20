# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_weakset.py
# case: TestWeakSet_test_add

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    x = ustr('Q')
    self.s.add(x)
    self.assertIn(x, self.s)
    dup = self.s.copy()
    self.s.add(x)
    self.assertEqual(self.s, dup)
    self.assertRaises(TypeError, self.s.add, [])
    self.fs.add(Foo())
    support.gc_collect()
    self.assertTrue(len(self.fs) == 1)
    self.fs.add(self.obj)
    self.assertTrue(len(self.fs) == 1)
