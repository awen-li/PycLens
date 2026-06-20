# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ipaddress.py
# case: ComparisonTests_test_foreign_type_ordering

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    other = object()
    for obj in self.objects_with_scoped:
        with self.assertRaises(TypeError):
            obj < other
        with self.assertRaises(TypeError):
            obj > other
        with self.assertRaises(TypeError):
            obj <= other
        with self.assertRaises(TypeError):
            obj >= other
        self.assertTrue(obj < LARGEST)
        self.assertFalse(obj > LARGEST)
        self.assertTrue(obj <= LARGEST)
        self.assertFalse(obj >= LARGEST)
        self.assertFalse(obj < SMALLEST)
        self.assertTrue(obj > SMALLEST)
        self.assertFalse(obj <= SMALLEST)
        self.assertTrue(obj >= SMALLEST)
