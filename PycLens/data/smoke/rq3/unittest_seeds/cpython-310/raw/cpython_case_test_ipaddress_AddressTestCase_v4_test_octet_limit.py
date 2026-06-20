# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ipaddress.py
# case: AddressTestCase_v4_test_octet_limit

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def assertBadOctet(addr, octet):
        msg = 'Octet %d (> 255) not permitted in %r' % (octet, addr)
        with self.assertAddressError(re.escape(msg)):
            ipaddress.IPv4Address(addr)
    assertBadOctet('257.0.0.0', 257)
    assertBadOctet('192.168.0.999', 999)
