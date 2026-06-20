# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_typing.py
# case: GenericTests_test_copy_generic_instances

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    T = TypeVar('T')

    class C(Generic[T]):

        def __init__(self, attr: T) -> None:
            self.attr = attr
    c = C(42)
    self.assertEqual(copy(c).attr, 42)
    self.assertEqual(deepcopy(c).attr, 42)
    self.assertIsNot(copy(c), c)
    self.assertIsNot(deepcopy(c), c)
    c.attr = 1
    self.assertEqual(copy(c).attr, 1)
    self.assertEqual(deepcopy(c).attr, 1)
    ci = C[int](42)
    self.assertEqual(copy(ci).attr, 42)
    self.assertEqual(deepcopy(ci).attr, 42)
    self.assertIsNot(copy(ci), ci)
    self.assertIsNot(deepcopy(ci), ci)
    ci.attr = 1
    self.assertEqual(copy(ci).attr, 1)
    self.assertEqual(deepcopy(ci).attr, 1)
    self.assertEqual(ci.__orig_class__, C[int])
