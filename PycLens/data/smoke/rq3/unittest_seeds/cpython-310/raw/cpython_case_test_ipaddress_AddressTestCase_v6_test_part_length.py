# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ipaddress.py
# case: AddressTestCase_v6_test_part_length

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def assertBadPart(addr, part):
        msg = 'At most 4 characters permitted in %r in %r'
        with self.assertAddressError(msg, part, addr.split('%')[0]):
            ipaddress.IPv6Address(addr)
    assertBadPart('::00000', '00000')
    assertBadPart('3ffe::10000', '10000')
    assertBadPart('02001:db8::', '02001')
    assertBadPart('2001:888888::1', '888888')
    assertBadPart('::00000%scope', '00000')
    assertBadPart('3ffe::10000%scope', '10000')
    assertBadPart('02001:db8::%scope', '02001')
    assertBadPart('2001:888888::1%scope', '888888')
