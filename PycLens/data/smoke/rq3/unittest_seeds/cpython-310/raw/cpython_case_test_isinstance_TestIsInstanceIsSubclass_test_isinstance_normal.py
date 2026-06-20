# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_isinstance.py
# case: TestIsInstanceIsSubclass_test_isinstance_normal

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertEqual(True, isinstance(Super(), Super))
    self.assertEqual(False, isinstance(Super(), Child))
    self.assertEqual(False, isinstance(Super(), AbstractSuper))
    self.assertEqual(False, isinstance(Super(), AbstractChild))
    self.assertEqual(True, isinstance(Child(), Super))
    self.assertEqual(False, isinstance(Child(), AbstractSuper))
