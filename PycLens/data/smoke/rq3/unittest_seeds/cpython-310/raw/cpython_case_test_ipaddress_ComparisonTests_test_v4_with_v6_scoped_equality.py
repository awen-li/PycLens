# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ipaddress.py
# case: ComparisonTests_test_v4_with_v6_scoped_equality

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for lhs in self.v4_objects:
        for rhs in self.v6_scoped_objects:
            self.assertNotEqual(lhs, rhs)
