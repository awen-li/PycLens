# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_typing.py
# case: GenericTests_test_implicit_any

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    T = TypeVar('T')

    class C(Generic[T]):
        pass

    class D(C):
        pass
    self.assertEqual(D.__parameters__, ())
    with self.assertRaises(TypeError):
        D[int]
    with self.assertRaises(TypeError):
        D[Any]
    with self.assertRaises(TypeError):
        D[T]
