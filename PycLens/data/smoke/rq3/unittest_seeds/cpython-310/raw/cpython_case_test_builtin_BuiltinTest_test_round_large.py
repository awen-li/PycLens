# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_builtin.py
# case: BuiltinTest_test_round_large

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertEqual(round(5000000000000000.0 - 1), 5000000000000000.0 - 1)
    self.assertEqual(round(5000000000000000.0), 5000000000000000.0)
    self.assertEqual(round(5000000000000000.0 + 1), 5000000000000000.0 + 1)
    self.assertEqual(round(5000000000000000.0 + 2), 5000000000000000.0 + 2)
    self.assertEqual(round(5000000000000000.0 + 3), 5000000000000000.0 + 3)
