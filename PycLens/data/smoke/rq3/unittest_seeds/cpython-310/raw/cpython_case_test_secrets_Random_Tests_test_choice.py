# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_secrets.py
# case: Random_Tests_test_choice

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    items = [1, 2, 4, 8, 16, 32, 64]
    for i in range(10):
        self.assertTrue(secrets.choice(items) in items)
