# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_urllib2.py
# case: RequestTests_test_proxy

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertFalse(self.get.has_proxy())
    self.get.set_proxy('www.perl.org', 'http')
    self.assertTrue(self.get.has_proxy())
    self.assertEqual('www.python.org', self.get.origin_req_host)
    self.assertEqual('www.perl.org', self.get.host)
