# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ipaddress.py
# case: AddressTestCase_v6_test_network_passed_as_address

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def assertBadSplit(addr):
        msg = "Unexpected '/' in %r"
        with self.assertAddressError(msg, addr):
            ipaddress.IPv6Address(addr)
    assertBadSplit('::1/24')
    assertBadSplit('::1%scope_id/24')
