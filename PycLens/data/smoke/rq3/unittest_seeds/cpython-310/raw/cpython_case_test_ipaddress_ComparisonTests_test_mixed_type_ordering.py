# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ipaddress.py
# case: ComparisonTests_test_mixed_type_ordering

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for lhs in self.objects_with_scoped:
        for rhs in self.objects_with_scoped:
            if isinstance(lhs, type(rhs)) or isinstance(rhs, type(lhs)):
                continue
            self.assertRaises(TypeError, lambda : lhs < rhs)
            self.assertRaises(TypeError, lambda : lhs > rhs)
            self.assertRaises(TypeError, lambda : lhs <= rhs)
            self.assertRaises(TypeError, lambda : lhs >= rhs)
