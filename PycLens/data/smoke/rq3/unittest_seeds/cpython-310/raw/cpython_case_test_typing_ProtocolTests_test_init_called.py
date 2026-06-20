# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_typing.py
# case: ProtocolTests_test_init_called

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    T = TypeVar('T')

    class P(Protocol[T]):
        pass

    class C(P[T]):

        def __init__(self):
            self.test = 'OK'
    self.assertEqual(C[int]().test, 'OK')

    class B:

        def __init__(self):
            self.test = 'OK'

    class D1(B, P[T]):
        pass
    self.assertEqual(D1[int]().test, 'OK')

    class D2(P[T], B):
        pass
    self.assertEqual(D2[int]().test, 'OK')
