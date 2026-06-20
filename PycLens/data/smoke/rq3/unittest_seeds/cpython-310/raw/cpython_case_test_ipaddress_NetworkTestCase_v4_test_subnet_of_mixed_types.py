# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ipaddress.py
# case: NetworkTestCase_v4_test_subnet_of_mixed_types

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with self.assertRaises(TypeError):
        ipaddress.IPv4Network('10.0.0.0/30').supernet_of(ipaddress.IPv6Network('::1/128'))
    with self.assertRaises(TypeError):
        ipaddress.IPv6Network('::1/128').supernet_of(ipaddress.IPv4Network('10.0.0.0/30'))
    with self.assertRaises(TypeError):
        ipaddress.IPv4Network('10.0.0.0/30').subnet_of(ipaddress.IPv6Network('::1/128'))
    with self.assertRaises(TypeError):
        ipaddress.IPv6Network('::1/128').subnet_of(ipaddress.IPv4Network('10.0.0.0/30'))
