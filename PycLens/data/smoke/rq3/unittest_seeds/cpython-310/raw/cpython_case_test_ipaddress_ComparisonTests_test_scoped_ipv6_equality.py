# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ipaddress.py
# case: ComparisonTests_test_scoped_ipv6_equality

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for (lhs, rhs) in zip(self.v6_objects, self.v6_scoped_objects):
        self.assertNotEqual(lhs, rhs)
