# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ipaddress.py
# case: ComparisonTests_test_same_type_ordering

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for (lhs, rhs) in ((self.v4addr, self.v4addr2), (self.v4net, self.v4net2), (self.v4intf, self.v4intf2), (self.v6addr, self.v6addr2), (self.v6net, self.v6net2), (self.v6intf, self.v6intf2), (self.v6addr_scoped, self.v6addr2_scoped), (self.v6net_scoped, self.v6net2_scoped), (self.v6intf_scoped, self.v6intf2_scoped)):
        self.assertNotEqual(lhs, rhs)
        self.assertLess(lhs, rhs)
        self.assertLessEqual(lhs, rhs)
        self.assertGreater(rhs, lhs)
        self.assertGreaterEqual(rhs, lhs)
        self.assertFalse(lhs > rhs)
        self.assertFalse(rhs < lhs)
        self.assertFalse(lhs >= rhs)
        self.assertFalse(rhs <= lhs)
