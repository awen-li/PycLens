# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ipaddress.py
# case: CommonTestMixin_v6_test_bad_packed_length

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def assertBadLength(length):
        addr = b'\x00' * length
        msg = '%r (len %d != 16) is not permitted as an IPv6 address'
        with self.assertAddressError(re.escape(msg % (addr, length))):
            self.factory(addr)
            self.factory(addr)
    assertBadLength(15)
    assertBadLength(17)
