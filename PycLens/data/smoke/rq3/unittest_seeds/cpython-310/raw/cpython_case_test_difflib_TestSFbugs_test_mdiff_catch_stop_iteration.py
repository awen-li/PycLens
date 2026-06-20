# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_difflib.py
# case: TestSFbugs_test_mdiff_catch_stop_iteration

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertEqual(list(difflib._mdiff(['2'], ['3'], 1)), [((1, '\x00-2\x01'), (1, '\x00+3\x01'), True)])
