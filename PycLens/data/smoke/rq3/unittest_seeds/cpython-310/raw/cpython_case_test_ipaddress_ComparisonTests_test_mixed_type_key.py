# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ipaddress.py
# case: ComparisonTests_test_mixed_type_key

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    v4_ordered = [self.v4addr, self.v4net, self.v4intf]
    v6_ordered = [self.v6addr, self.v6net, self.v6intf]
    v6_scoped_ordered = [self.v6addr_scoped, self.v6net_scoped, self.v6intf_scoped]
    self.assertEqual(v4_ordered, sorted(self.v4_objects, key=ipaddress.get_mixed_type_key))
    self.assertEqual(v6_ordered, sorted(self.v6_objects, key=ipaddress.get_mixed_type_key))
    self.assertEqual(v6_scoped_ordered, sorted(self.v6_scoped_objects, key=ipaddress.get_mixed_type_key))
    self.assertEqual(v4_ordered + v6_scoped_ordered, sorted(self.v4_objects + self.v6_scoped_objects, key=ipaddress.get_mixed_type_key))
    self.assertEqual(NotImplemented, ipaddress.get_mixed_type_key(object))
