# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ipaddress.py
# case: AddressTestCase_v4_test_empty_octet

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def assertBadOctet(addr):
        with self.assertAddressError('Empty octet not permitted in %r', addr):
            ipaddress.IPv4Address(addr)
    assertBadOctet('42..42.42')
    assertBadOctet('...')
