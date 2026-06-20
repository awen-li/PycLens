# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ipaddress.py
# case: NetmaskTestMixin_v4_test_split_netmask

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    addr = '1.2.3.4/32/24'
    with self.assertAddressError("Only one '/' permitted in %r" % addr):
        self.factory(addr)
