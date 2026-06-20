# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_typing.py
# case: ParamSpecTests_test_multiple_paramspecs_in_user_generics

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    P = ParamSpec('P')
    P2 = ParamSpec('P2')

    class X(Generic[P, P2]):
        f: Callable[P, int]
        g: Callable[P2, str]
    G1 = X[[int, str], [bytes]]
    G2 = X[[int], [str, bytes]]
    self.assertNotEqual(G1, G2)
    self.assertEqual(G1.__args__, ((int, str), (bytes,)))
    self.assertEqual(G2.__args__, ((int,), (str, bytes)))
