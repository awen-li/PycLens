# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_isinstance.py
# case: TestIsInstanceIsSubclass_test_subclass_normal

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertEqual(True, issubclass(Super, Super))
    self.assertEqual(False, issubclass(Super, AbstractSuper))
    self.assertEqual(False, issubclass(Super, Child))
    self.assertEqual(True, issubclass(Child, Child))
    self.assertEqual(True, issubclass(Child, Super))
    self.assertEqual(False, issubclass(Child, AbstractSuper))
    self.assertTrue(issubclass(typing.List, typing.List | typing.Tuple))
    self.assertFalse(issubclass(int, typing.List | typing.Tuple))
