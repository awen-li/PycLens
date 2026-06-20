# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ipaddress.py
# case: AddressTestCase_v6_test_bad_address_split_v6_too_many_parts

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def assertBadSplit(addr):
        msg = "Exactly 8 parts expected without '::' in %r"
        with self.assertAddressError(msg, addr.split('%')[0]):
            ipaddress.IPv6Address(addr)
    assertBadSplit('3ffe:0:0:0:0:0:0:0:1')
    assertBadSplit('9:8:7:6:5:4:3:2:1')
    assertBadSplit('7:6:5:4:3:2:1')
    assertBadSplit('9:8:7:6:5:4:3:42.42.42.42')
    assertBadSplit('7:6:5:4:3:42.42.42.42')
    assertBadSplit('3ffe:0:0:0:0:0:0:0:1%scope')
    assertBadSplit('9:8:7:6:5:4:3:2:1%scope')
    assertBadSplit('7:6:5:4:3:2:1%scope')
    assertBadSplit('9:8:7:6:5:4:3:42.42.42.42%scope')
    assertBadSplit('7:6:5:4:3:42.42.42.42%scope')
