# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_isinstance.py
# case: TestIsInstanceIsSubclass_test_subclass_abstract

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertEqual(True, issubclass(AbstractSuper, AbstractSuper))
    self.assertEqual(False, issubclass(AbstractSuper, AbstractChild))
    self.assertEqual(False, issubclass(AbstractSuper, Child))
    self.assertEqual(True, issubclass(AbstractChild, AbstractChild))
    self.assertEqual(True, issubclass(AbstractChild, AbstractSuper))
    self.assertEqual(False, issubclass(AbstractChild, Super))
    self.assertEqual(False, issubclass(AbstractChild, Child))
