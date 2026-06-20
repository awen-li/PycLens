# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ipaddress.py
# case: AddressTestCase_v6_test_bad_address_split_v6_leading_colon

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def assertBadSplit(addr):
        msg = "Leading ':' only permitted as part of '::' in %r"
        with self.assertAddressError(msg, addr.split('%')[0]):
            ipaddress.IPv6Address(addr)
    assertBadSplit(':2001:db8::1')
    assertBadSplit(':1:2:3:4:5:6:7')
    assertBadSplit(':1:2:3:4:5:6:')
    assertBadSplit(':6:5:4:3:2:1::')
    assertBadSplit(':2001:db8::1%scope')
    assertBadSplit(':1:2:3:4:5:6:7%scope')
    assertBadSplit(':1:2:3:4:5:6:%scope')
    assertBadSplit(':6:5:4:3:2:1::%scope')
