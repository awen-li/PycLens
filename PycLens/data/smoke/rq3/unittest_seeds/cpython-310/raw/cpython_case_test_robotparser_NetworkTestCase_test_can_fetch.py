# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_robotparser.py
# case: NetworkTestCase_test_can_fetch

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertTrue(self.parser.can_fetch('*', self.url('elsewhere')))
    self.assertFalse(self.parser.can_fetch('Nutch', self.base_url))
    self.assertFalse(self.parser.can_fetch('Nutch', self.url('brian')))
    self.assertFalse(self.parser.can_fetch('Nutch', self.url('webstats')))
    self.assertFalse(self.parser.can_fetch('*', self.url('webstats')))
    self.assertTrue(self.parser.can_fetch('*', self.base_url))
