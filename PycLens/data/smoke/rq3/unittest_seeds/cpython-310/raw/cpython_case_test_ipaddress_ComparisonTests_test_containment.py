# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ipaddress.py
# case: ComparisonTests_test_containment

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for obj in self.v4_addresses:
        self.assertIn(obj, self.v4net)
    for obj in self.v6_addresses + self.v6_scoped_addresses:
        self.assertIn(obj, self.v6net)
    for obj in self.v6_addresses + self.v6_scoped_addresses:
        self.assertIn(obj, self.v6net_scoped)
    for obj in self.v4_objects + [self.v6net, self.v6net_scoped]:
        self.assertNotIn(obj, self.v6net)
    for obj in self.v4_objects + [self.v6net, self.v6net_scoped]:
        self.assertNotIn(obj, self.v6net_scoped)
    for obj in self.v6_objects + self.v6_scoped_objects + [self.v4net]:
        self.assertNotIn(obj, self.v4net)
