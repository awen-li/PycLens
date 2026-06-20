# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_enum.py
# case: TestHelpers_test_dunder

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for name in self.dunder_names:
        self.assertTrue(enum._is_dunder(name), '%r is a not dunder name?' % name)
    for name in self.sunder_names + self.private_names + self.private_and_sunder_names + self.random_names:
        self.assertFalse(enum._is_dunder(name), '%r is a dunder name?' % name)
