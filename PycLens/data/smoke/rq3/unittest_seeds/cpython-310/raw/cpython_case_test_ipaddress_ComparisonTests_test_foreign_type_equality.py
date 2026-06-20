# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ipaddress.py
# case: ComparisonTests_test_foreign_type_equality

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    other = object()
    for obj in self.objects_with_scoped:
        self.assertNotEqual(obj, other)
        self.assertFalse(obj == other)
        self.assertEqual(obj.__eq__(other), NotImplemented)
        self.assertEqual(obj.__ne__(other), NotImplemented)
