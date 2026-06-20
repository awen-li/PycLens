# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ipaddress.py
# case: NetmaskTestMixin_v6_test_split_netmask

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    addr = 'cafe:cafe::/128/190'
    with self.assertAddressError("Only one '/' permitted in %r" % addr):
        self.factory(addr)
    scoped_addr = 'cafe:cafe::%scope/128/190'
    with self.assertAddressError("Only one '/' permitted in %r" % scoped_addr):
        self.factory(scoped_addr)
