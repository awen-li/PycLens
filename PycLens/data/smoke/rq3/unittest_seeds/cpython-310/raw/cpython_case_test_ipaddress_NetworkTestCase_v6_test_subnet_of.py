# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ipaddress.py
# case: NetworkTestCase_v6_test_subnet_of

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertFalse(self.factory('2000:999::/56').subnet_of(self.factory('2000:aaa::/48')))
    self.assertTrue(self.factory('2000:aaa::/56').subnet_of(self.factory('2000:aaa::/48')))
    self.assertFalse(self.factory('2000:bbb::/56').subnet_of(self.factory('2000:aaa::/48')))
    self.assertFalse(self.factory('2000:aaa::/48').subnet_of(self.factory('2000:aaa::/56')))
    self.assertFalse(self.factory('2000:999::%scope/56').subnet_of(self.factory('2000:aaa::%scope/48')))
    self.assertTrue(self.factory('2000:aaa::%scope/56').subnet_of(self.factory('2000:aaa::%scope/48')))
