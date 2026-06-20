# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ipaddress.py
# case: CommonTestMixin_v4_test_packed

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertInstancesEqual(bytes.fromhex('00000000'), '0.0.0.0')
    self.assertInstancesEqual(bytes.fromhex('c0a80001'), '192.168.0.1')
