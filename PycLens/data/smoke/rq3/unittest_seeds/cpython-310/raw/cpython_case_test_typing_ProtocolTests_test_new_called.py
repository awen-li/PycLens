# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_typing.py
# case: ProtocolTests_test_new_called

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    T = TypeVar('T')

    class P(Protocol[T]):
        pass

    class C(P[T]):

        def __new__(cls, *args):
            self = super().__new__(cls, *args)
            self.test = 'OK'
            return self
    self.assertEqual(C[int]().test, 'OK')
    with self.assertRaises(TypeError):
        C[int](42)
    with self.assertRaises(TypeError):
        C[int](a=42)
