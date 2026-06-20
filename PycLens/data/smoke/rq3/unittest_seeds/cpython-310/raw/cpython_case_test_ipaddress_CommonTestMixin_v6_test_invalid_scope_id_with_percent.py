# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ipaddress.py
# case: CommonTestMixin_v6_test_invalid_scope_id_with_percent

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    address = '::1%scope%'
    with self.assertAddressError('Invalid IPv6 address: "%r"', address):
        self.factory(address)
