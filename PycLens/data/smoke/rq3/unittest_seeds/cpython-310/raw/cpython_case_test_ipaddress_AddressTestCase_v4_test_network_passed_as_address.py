# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ipaddress.py
# case: AddressTestCase_v4_test_network_passed_as_address

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    addr = '127.0.0.1/24'
    with self.assertAddressError("Unexpected '/' in %r", addr):
        ipaddress.IPv4Address(addr)
