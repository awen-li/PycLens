# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_positional_only_arg.py
# case: PositionalOnlyTestCase_test_lambdas

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    x = lambda a, /, b: a + b
    self.assertEqual(x(1, 2), 3)
    self.assertEqual(x(1, b=2), 3)
    x = lambda a, /, b=2: a + b
    self.assertEqual(x(1), 3)
    x = lambda a, b, /: a + b
    self.assertEqual(x(1, 2), 3)
    x = lambda a, b, /: a + b
    self.assertEqual(x(1, 2), 3)
