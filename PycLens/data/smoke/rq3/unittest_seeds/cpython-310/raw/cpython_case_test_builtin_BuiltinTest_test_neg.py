# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_builtin.py
# case: BuiltinTest_test_neg

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    x = -sys.maxsize - 1
    self.assertTrue(isinstance(x, int))
    self.assertEqual(-x, sys.maxsize + 1)
