# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_re.py
# case: ReTests_test_constants

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertEqual(re.I, re.IGNORECASE)
    self.assertEqual(re.L, re.LOCALE)
    self.assertEqual(re.M, re.MULTILINE)
    self.assertEqual(re.S, re.DOTALL)
    self.assertEqual(re.X, re.VERBOSE)
