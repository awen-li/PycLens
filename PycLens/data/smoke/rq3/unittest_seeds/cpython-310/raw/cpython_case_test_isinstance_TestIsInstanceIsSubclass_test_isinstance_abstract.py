# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_isinstance.py
# case: TestIsInstanceIsSubclass_test_isinstance_abstract

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertEqual(True, isinstance(AbstractSuper(), AbstractSuper))
    self.assertEqual(False, isinstance(AbstractSuper(), AbstractChild))
    self.assertEqual(False, isinstance(AbstractSuper(), Super))
    self.assertEqual(False, isinstance(AbstractSuper(), Child))
    self.assertEqual(True, isinstance(AbstractChild(), AbstractChild))
    self.assertEqual(True, isinstance(AbstractChild(), AbstractSuper))
    self.assertEqual(False, isinstance(AbstractChild(), Super))
    self.assertEqual(False, isinstance(AbstractChild(), Child))
