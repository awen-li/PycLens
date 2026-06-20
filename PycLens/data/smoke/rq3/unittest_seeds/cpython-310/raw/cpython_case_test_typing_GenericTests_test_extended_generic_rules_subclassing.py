# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_typing.py
# case: GenericTests_test_extended_generic_rules_subclassing

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class T1(Tuple[T, KT]):
        ...

    class T2(Tuple[T, ...]):
        ...

    class C1(typing.Container[T]):

        def __contains__(self, item):
            return False
    self.assertEqual(T1.__parameters__, (T, KT))
    self.assertEqual(T1[int, str].__args__, (int, str))
    self.assertEqual(T1[int, T].__origin__, T1)
    self.assertEqual(T2.__parameters__, (T,))
    self.assertEqual(repr(C1[int]).split('.')[-1], 'C1[int]')
    self.assertEqual(C1.__parameters__, (T,))
    self.assertIsInstance(C1(), collections.abc.Container)
    self.assertIsSubclass(C1, collections.abc.Container)
    self.assertIsInstance(T1(), tuple)
    self.assertIsSubclass(T2, tuple)
    with self.assertRaises(TypeError):
        issubclass(Tuple[int, ...], typing.Sequence)
    with self.assertRaises(TypeError):
        issubclass(Tuple[int, ...], typing.Iterable)
