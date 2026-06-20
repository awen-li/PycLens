# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ipaddress.py
# case: NetmaskTestMixin_v4_test_no_mask

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for address in ('1.2.3.4', 16909060, b'\x01\x02\x03\x04'):
        net = self.factory(address)
        self.assertEqual(str(net), '1.2.3.4/32')
        self.assertEqual(str(net.netmask), '255.255.255.255')
        self.assertEqual(str(net.hostmask), '0.0.0.0')
