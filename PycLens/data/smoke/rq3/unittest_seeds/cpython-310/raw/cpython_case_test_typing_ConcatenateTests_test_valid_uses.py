# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_typing.py
# case: ConcatenateTests_test_valid_uses

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    P = ParamSpec('P')
    T = TypeVar('T')
    C1 = Callable[Concatenate[int, P], int]
    self.assertEqual(C1.__args__, (Concatenate[int, P], int))
    self.assertEqual(C1.__parameters__, (P,))
    C2 = Callable[Concatenate[int, T, P], T]
    self.assertEqual(C2.__args__, (Concatenate[int, T, P], T))
    self.assertEqual(C2.__parameters__, (T, P))
    C3 = collections.abc.Callable[Concatenate[int, P], int]
    self.assertEqual(C3.__args__, (Concatenate[int, P], int))
    self.assertEqual(C3.__parameters__, (P,))
    C4 = collections.abc.Callable[Concatenate[int, T, P], T]
    self.assertEqual(C4.__args__, (Concatenate[int, T, P], T))
    self.assertEqual(C4.__parameters__, (T, P))
