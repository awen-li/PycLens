# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ipaddress.py
# case: NetworkTestCase_v4_test_subnet_of

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertFalse(self.factory('10.0.0.0/30').subnet_of(self.factory('10.0.1.0/24')))
    self.assertTrue(self.factory('10.0.0.0/30').subnet_of(self.factory('10.0.0.0/24')))
    self.assertFalse(self.factory('10.0.0.0/30').subnet_of(self.factory('10.0.1.0/24')))
    self.assertFalse(self.factory('10.0.1.0/24').subnet_of(self.factory('10.0.0.0/30')))
