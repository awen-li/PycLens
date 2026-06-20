# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_enum.py
# case: TestHelpers_test_is_sunder

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for s in ('_a_', '_aa_'):
        self.assertTrue(enum._is_sunder(s))
    for s in ('a', 'a_', '_a', '__a', 'a__', '__a__', '_a__', '__a_', '_', '__', '___', '____', '_____'):
        self.assertFalse(enum._is_sunder(s))
