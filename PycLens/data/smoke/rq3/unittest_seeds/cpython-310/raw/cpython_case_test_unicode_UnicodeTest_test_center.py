# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_unicode.py
# case: UnicodeTest_test_center

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    string_tests.CommonTest.test_center(self)
    self.assertEqual('x'.center(2, '\U0010ffff'), 'x\U0010ffff')
    self.assertEqual('x'.center(3, '\U0010ffff'), '\U0010ffffx\U0010ffff')
    self.assertEqual('x'.center(4, '\U0010ffff'), '\U0010ffffx\U0010ffff\U0010ffff')
