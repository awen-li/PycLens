# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_typing.py
# case: GenericTests_test_chain_repr

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    T = TypeVar('T')
    S = TypeVar('S')

    class C(Generic[T]):
        pass
    X = C[Tuple[S, T]]
    self.assertEqual(X, C[Tuple[S, T]])
    self.assertNotEqual(X, C[Tuple[T, S]])
    Y = X[T, int]
    self.assertEqual(Y, X[T, int])
    self.assertNotEqual(Y, X[S, int])
    self.assertNotEqual(Y, X[T, str])
    Z = Y[str]
    self.assertEqual(Z, Y[str])
    self.assertNotEqual(Z, Y[int])
    self.assertNotEqual(Z, Y[T])
    self.assertTrue(str(Z).endswith('.C[typing.Tuple[str, int]]'))
