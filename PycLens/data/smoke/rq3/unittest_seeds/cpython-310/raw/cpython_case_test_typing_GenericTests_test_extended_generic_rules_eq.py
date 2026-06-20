# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_typing.py
# case: GenericTests_test_extended_generic_rules_eq

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    T = TypeVar('T')
    U = TypeVar('U')
    self.assertEqual(Tuple[T, T][int], Tuple[int, int])
    self.assertEqual(typing.Iterable[Tuple[T, T]][T], typing.Iterable[Tuple[T, T]])
    with self.assertRaises(TypeError):
        Tuple[T, int][()]
    self.assertEqual(Union[T, int][int], int)
    self.assertEqual(Union[T, U][int, Union[int, str]], Union[int, str])

    class Base:
        ...

    class Derived(Base):
        ...
    self.assertEqual(Union[T, Base][Union[Base, Derived]], Union[Base, Derived])
    with self.assertRaises(TypeError):
        Union[T, int][1]
    self.assertEqual(Callable[[T], T][KT], Callable[[KT], KT])
    self.assertEqual(Callable[..., List[T]][int], Callable[..., List[int]])
