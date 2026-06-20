# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ipaddress.py
# case: AddressTestCase_v4_test_octet_length

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def assertBadOctet(addr, octet):
        msg = 'At most 3 characters permitted in %r in %r'
        with self.assertAddressError(re.escape(msg % (octet, addr))):
            ipaddress.IPv4Address(addr)
    assertBadOctet('0000.000.000.000', '0000')
    assertBadOctet('12345.67899.-54321.-98765', '12345')
