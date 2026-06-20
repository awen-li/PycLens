# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ipaddress.py
# case: AddressTestCase_v4_test_invalid_characters

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def assertBadOctet(addr, octet):
        msg = 'Only decimal digits permitted in %r in %r' % (octet, addr)
        with self.assertAddressError(re.escape(msg)):
            ipaddress.IPv4Address(addr)
    assertBadOctet('0x0a.0x0a.0x0a.0x0a', '0x0a')
    assertBadOctet('0xa.0x0a.0x0a.0x0a', '0xa')
    assertBadOctet('42.42.42.-0', '-0')
    assertBadOctet('42.42.42.+0', '+0')
    assertBadOctet('42.42.42.-42', '-42')
    assertBadOctet('+1.+2.+3.4', '+1')
    assertBadOctet('1.2.3.4e0', '4e0')
    assertBadOctet('1.2.3.4::', '4::')
    assertBadOctet('1.a.2.3', 'a')
