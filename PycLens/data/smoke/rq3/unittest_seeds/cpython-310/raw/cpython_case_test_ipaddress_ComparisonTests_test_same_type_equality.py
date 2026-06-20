# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ipaddress.py
# case: ComparisonTests_test_same_type_equality

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for obj in self.objects_with_scoped:
        self.assertEqual(obj, obj)
        self.assertLessEqual(obj, obj)
        self.assertGreaterEqual(obj, obj)
