# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ipaddress.py
# case: NetmaskTestMixin_v4_test_address_errors

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def assertBadAddress(addr, details):
        with self.assertAddressError(details):
            self.factory(addr)
    assertBadAddress('/', 'Address cannot be empty')
    assertBadAddress('/8', 'Address cannot be empty')
    assertBadAddress('bogus', 'Expected 4 octets')
    assertBadAddress('google.com', 'Expected 4 octets')
    assertBadAddress('10/8', 'Expected 4 octets')
    assertBadAddress('::1.2.3.4', 'Only decimal digits')
    assertBadAddress('1.2.3.256', re.escape('256 (> 255)'))
