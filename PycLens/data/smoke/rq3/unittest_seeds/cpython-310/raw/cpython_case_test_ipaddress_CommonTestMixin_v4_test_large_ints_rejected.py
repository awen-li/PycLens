# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ipaddress.py
# case: CommonTestMixin_v4_test_large_ints_rejected

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    msg = '%d (>= 2**32) is not permitted as an IPv4 address'
    with self.assertAddressError(re.escape(msg % 2 ** 32)):
        self.factory(2 ** 32)
