# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ipaddress.py
# case: AddressTestCase_v6_test_invalid_characters

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def assertBadPart(addr, part):
        msg = 'Only hex digits permitted in %r in %r' % (part, addr.split('%')[0])
        with self.assertAddressError(re.escape(msg)):
            ipaddress.IPv6Address(addr)
    assertBadPart('3ffe::goog', 'goog')
    assertBadPart('3ffe::-0', '-0')
    assertBadPart('3ffe::+0', '+0')
    assertBadPart('3ffe::-1', '-1')
    assertBadPart('1.2.3.4::', '1.2.3.4')
    assertBadPart('1234:axy::b', 'axy')
    assertBadPart('3ffe::goog%scope', 'goog')
    assertBadPart('3ffe::-0%scope', '-0')
    assertBadPart('3ffe::+0%scope', '+0')
    assertBadPart('3ffe::-1%scope', '-1')
    assertBadPart('1.2.3.4::%scope', '1.2.3.4')
    assertBadPart('1234:axy::b%scope', 'axy')
