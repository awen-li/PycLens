# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_isinstance.py
# case: TestIsInstanceIsSubclass_test_subclass_with_union

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertTrue(issubclass(int, int | float | int))
    self.assertTrue(issubclass(str, str | Child | str))
    self.assertFalse(issubclass(dict, float | str))
    self.assertFalse(issubclass(object, float | str))
    with self.assertRaises(TypeError):
        issubclass(2, Child | Super)
    with self.assertRaises(TypeError):
        issubclass(int, list[int] | Child)
