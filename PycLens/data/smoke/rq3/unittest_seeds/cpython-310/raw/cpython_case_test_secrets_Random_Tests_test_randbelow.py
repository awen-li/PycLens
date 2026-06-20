# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_secrets.py
# case: Random_Tests_test_randbelow

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for i in range(2, 10):
        self.assertIn(secrets.randbelow(i), range(i))
    self.assertRaises(ValueError, secrets.randbelow, 0)
    self.assertRaises(ValueError, secrets.randbelow, -1)
