# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_isinstance.py
# case: TestIsInstanceIsSubclass_test_isinstance_with_or_union

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertTrue(isinstance(Super(), Super | int))
    self.assertFalse(isinstance(None, str | int))
    self.assertTrue(isinstance(3, str | int))
    self.assertTrue(isinstance('', str | int))
    self.assertTrue(isinstance([], typing.List | typing.Tuple))
    self.assertTrue(isinstance(2, typing.List | int))
    self.assertFalse(isinstance(2, typing.List | typing.Tuple))
    self.assertTrue(isinstance(None, int | None))
    self.assertFalse(isinstance(3.14, int | str))
    with self.assertRaises(TypeError):
        isinstance(2, list[int])
    with self.assertRaises(TypeError):
        isinstance(2, list[int] | int)
    with self.assertRaises(TypeError):
        isinstance(2, int | str | list[int] | float)
