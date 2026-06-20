# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ipaddress.py
# case: NetmaskTestMixin_v6_test_no_mask

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for address in ('::1', 1, b'\x00' * 15 + b'\x01'):
        net = self.factory(address)
        self.assertEqual(str(net), '::1/128')
        self.assertEqual(str(net.netmask), 'ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff')
        self.assertEqual(str(net.hostmask), '::')
    scoped_net = self.factory('::1%scope')
    self.assertEqual(str(scoped_net), '::1%scope/128')
    self.assertEqual(str(scoped_net.netmask), 'ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff')
    self.assertEqual(str(scoped_net.hostmask), '::')
