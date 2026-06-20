# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ipaddress.py
# case: NetmaskTestMixin_v6_test_address_errors

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def assertBadAddress(addr, details):
        with self.assertAddressError(details):
            self.factory(addr)
    assertBadAddress('/', 'Address cannot be empty')
    assertBadAddress('/8', 'Address cannot be empty')
    assertBadAddress('google.com', 'At least 3 parts')
    assertBadAddress('1.2.3.4', 'At least 3 parts')
    assertBadAddress('10/8', 'At least 3 parts')
    assertBadAddress('1234:axy::b', 'Only hex digits')
    assertBadAddress('/%scope', 'Address cannot be empty')
    assertBadAddress('/%scope8', 'Address cannot be empty')
    assertBadAddress('google.com%scope', 'At least 3 parts')
    assertBadAddress('1.2.3.4%scope', 'At least 3 parts')
    assertBadAddress('10%scope/8', 'At least 3 parts')
    assertBadAddress('1234:axy::b%scope', 'Only hex digits')
