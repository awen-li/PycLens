# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ipaddress.py
# case: ComparisonTests_test_incompatible_versions

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    v4addr = ipaddress.ip_address('1.1.1.1')
    v4net = ipaddress.ip_network('1.1.1.1')
    v6addr = ipaddress.ip_address('::1')
    v6net = ipaddress.ip_network('::1')
    v6addr_scoped = ipaddress.ip_address('::1%scope')
    v6net_scoped = ipaddress.ip_network('::1%scope')
    self.assertRaises(TypeError, v4addr.__lt__, v6addr)
    self.assertRaises(TypeError, v4addr.__gt__, v6addr)
    self.assertRaises(TypeError, v4net.__lt__, v6net)
    self.assertRaises(TypeError, v4net.__gt__, v6net)
    self.assertRaises(TypeError, v6addr.__lt__, v4addr)
    self.assertRaises(TypeError, v6addr.__gt__, v4addr)
    self.assertRaises(TypeError, v6net.__lt__, v4net)
    self.assertRaises(TypeError, v6net.__gt__, v4net)
    self.assertRaises(TypeError, v4addr.__lt__, v6addr_scoped)
    self.assertRaises(TypeError, v4addr.__gt__, v6addr_scoped)
    self.assertRaises(TypeError, v4net.__lt__, v6net_scoped)
    self.assertRaises(TypeError, v4net.__gt__, v6net_scoped)
    self.assertRaises(TypeError, v6addr_scoped.__lt__, v4addr)
    self.assertRaises(TypeError, v6addr_scoped.__gt__, v4addr)
    self.assertRaises(TypeError, v6net_scoped.__lt__, v4net)
    self.assertRaises(TypeError, v6net_scoped.__gt__, v4net)
