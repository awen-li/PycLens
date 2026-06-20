# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_robotparser.py
# case: NetworkTestCase_test_basic

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertFalse(self.parser.disallow_all)
    self.assertFalse(self.parser.allow_all)
    self.assertGreater(self.parser.mtime(), 0)
    self.assertFalse(self.parser.crawl_delay('*'))
    self.assertFalse(self.parser.request_rate('*'))
