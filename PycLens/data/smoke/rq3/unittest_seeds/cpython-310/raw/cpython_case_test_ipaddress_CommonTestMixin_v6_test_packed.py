# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ipaddress.py
# case: CommonTestMixin_v6_test_packed

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    addr = b'\x00' * 12 + bytes.fromhex('00000000')
    self.assertInstancesEqual(addr, '::')
    addr = b'\x00' * 12 + bytes.fromhex('c0a80001')
    self.assertInstancesEqual(addr, '::c0a8:1')
    addr = bytes.fromhex('c0a80001') + b'\x00' * 12
    self.assertInstancesEqual(addr, 'c0a8:1::')
