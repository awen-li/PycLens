# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_dataclasses.py
# case: TestCase_test_generic_dynamic

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    T = TypeVar('T')

    @dataclass
    class Parent(Generic[T]):
        x: T
    Child = make_dataclass('Child', [('y', T), ('z', Optional[T], None)], bases=(Parent[int], Generic[T]), namespace={'other': 42})
    self.assertIs(Child[int](1, 2).z, None)
    self.assertEqual(Child[int](1, 2, 3).z, 3)
    self.assertEqual(Child[int](1, 2, 3).other, 42)
    Alias = Child[T]
    self.assertEqual(Alias[int](1, 2).x, 1)
    self.assertEqual(Child.__mro__, (Child, Parent, Generic, object))
