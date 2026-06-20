# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ipaddress.py
# case: AddressTestCase_v6_test_bad_address_split_v6_too_many_parts_with_double_colon

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def assertBadSplit(addr):
        msg = "Expected at most 7 other parts with '::' in %r"
        with self.assertAddressError(msg, addr.split('%')[0]):
            ipaddress.IPv6Address(addr)
    assertBadSplit('1:2:3:4::5:6:7:8')
    assertBadSplit('1:2:3:4::5:6:7:8%scope')
