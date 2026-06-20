# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_isinstance.py
# case: TestIsInstanceIsSubclass_test_subclass_tuple

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertEqual(True, issubclass(Child, (Child,)))
    self.assertEqual(True, issubclass(Child, (Super,)))
    self.assertEqual(False, issubclass(Super, (Child,)))
    self.assertEqual(True, issubclass(Super, (Child, Super)))
    self.assertEqual(False, issubclass(Child, ()))
    self.assertEqual(True, issubclass(Super, (Child, (Super,))))
    self.assertEqual(True, issubclass(int, (int, (float, int))))
    self.assertEqual(True, issubclass(str, (str, (Child, str))))
