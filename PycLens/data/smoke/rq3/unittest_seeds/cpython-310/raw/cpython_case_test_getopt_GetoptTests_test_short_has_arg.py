# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_getopt.py
# case: GetoptTests_test_short_has_arg

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertTrue(getopt.short_has_arg('a', 'a:'))
    self.assertFalse(getopt.short_has_arg('a', 'a'))
    self.assertError(getopt.short_has_arg, 'a', 'b')
