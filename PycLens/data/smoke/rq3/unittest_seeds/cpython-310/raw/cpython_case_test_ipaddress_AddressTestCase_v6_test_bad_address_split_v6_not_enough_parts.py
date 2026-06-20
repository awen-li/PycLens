# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ipaddress.py
# case: AddressTestCase_v6_test_bad_address_split_v6_not_enough_parts

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def assertBadSplit(addr):
        msg = 'At least 3 parts expected in %r'
        with self.assertAddressError(msg, addr.split('%')[0]):
            ipaddress.IPv6Address(addr)
    assertBadSplit(':')
    assertBadSplit(':1')
    assertBadSplit('FEDC:9878')
    assertBadSplit(':%scope')
    assertBadSplit(':1%scope')
    assertBadSplit('FEDC:9878%scope')
