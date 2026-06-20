# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ipaddress.py
# case: AddressTestCase_v6_test_bad_v4_part_in

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def assertBadAddressPart(addr, v4_error):
        with self.assertAddressError('%s in %r', v4_error, addr.split('%')[0]):
            ipaddress.IPv6Address(addr)
    assertBadAddressPart('3ffe::1.net', "Expected 4 octets in '1.net'")
    assertBadAddressPart('3ffe::127.0.1', "Expected 4 octets in '127.0.1'")
    assertBadAddressPart('::1.2.3', "Expected 4 octets in '1.2.3'")
    assertBadAddressPart('::1.2.3.4.5', "Expected 4 octets in '1.2.3.4.5'")
    assertBadAddressPart('3ffe::1.1.1.net', "Only decimal digits permitted in 'net' in '1.1.1.net'")
    assertBadAddressPart('3ffe::1.net%scope', "Expected 4 octets in '1.net'")
    assertBadAddressPart('3ffe::127.0.1%scope', "Expected 4 octets in '127.0.1'")
    assertBadAddressPart('::1.2.3%scope', "Expected 4 octets in '1.2.3'")
    assertBadAddressPart('::1.2.3.4.5%scope', "Expected 4 octets in '1.2.3.4.5'")
    assertBadAddressPart('3ffe::1.1.1.net%scope', "Only decimal digits permitted in 'net' in '1.1.1.net'")
