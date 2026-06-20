# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_set.py
# case: TestSet_test_init

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    s = self.thetype()
    s.__init__(self.word)
    self.assertEqual(s, set(self.word))
    s.__init__(self.otherword)
    self.assertEqual(s, set(self.otherword))
    self.assertRaises(TypeError, s.__init__, s, 2)
    self.assertRaises(TypeError, s.__init__, 1)
