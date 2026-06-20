# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_optparse.py
# case: TestOptionParser_test_get_option_equals

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    opt1 = self.parser.get_option('-v')
    opt2 = self.parser.get_option('--verbose')
    opt3 = self.parser.get_option('-n')
    opt4 = self.parser.get_option('--noisy')
    self.assertTrue(opt1 is opt2 is opt3 is opt4)
