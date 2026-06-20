# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_weakset.py
# case: TestWeakSet_test_init

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    s = WeakSet()
    s.__init__(self.items)
    self.assertEqual(s, self.s)
    s.__init__(self.items2)
    self.assertEqual(s, WeakSet(self.items2))
    self.assertRaises(TypeError, s.__init__, s, 2)
    self.assertRaises(TypeError, s.__init__, 1)
