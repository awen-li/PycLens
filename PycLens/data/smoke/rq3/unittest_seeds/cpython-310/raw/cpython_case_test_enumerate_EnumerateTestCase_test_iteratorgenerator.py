# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_enumerate.py
# case: EnumerateTestCase_test_iteratorgenerator

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertEqual(list(self.enum(Ig(self.seq))), self.res)
    e = self.enum(Ig(''))
    self.assertRaises(StopIteration, next, e)
