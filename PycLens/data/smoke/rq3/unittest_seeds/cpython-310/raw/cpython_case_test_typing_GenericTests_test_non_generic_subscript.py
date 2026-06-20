# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_typing.py
# case: GenericTests_test_non_generic_subscript

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    T = TypeVar('T')

    class G(Generic[T]):
        pass
    for s in (int, G, List, list, TypeVar, ParamSpec, types.GenericAlias, types.UnionType):
        for t in (Tuple, tuple):
            with self.subTest(tuple=t, sub=s):
                self.assertEqual(t[s, T][int], t[s, int])
                self.assertEqual(t[T, s][int], t[int, s])
                a = t[s]
                with self.assertRaises(TypeError):
                    a[int]
        for c in (Callable, collections.abc.Callable):
            with self.subTest(callable=c, sub=s):
                self.assertEqual(c[[s], T][int], c[[s], int])
                self.assertEqual(c[[T], s][int], c[[int], s])
                a = c[[s], s]
                with self.assertRaises(TypeError):
                    a[int]
