# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_typing.py
# case: ParamSpecTests_test_valid_uses

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    P = ParamSpec('P')
    T = TypeVar('T')
    C1 = Callable[P, int]
    self.assertEqual(C1.__args__, (P, int))
    self.assertEqual(C1.__parameters__, (P,))
    C2 = Callable[P, T]
    self.assertEqual(C2.__args__, (P, T))
    self.assertEqual(C2.__parameters__, (P, T))
    C3 = collections.abc.Callable[P, int]
    self.assertEqual(C3.__args__, (P, int))
    self.assertEqual(C3.__parameters__, (P,))
    C4 = collections.abc.Callable[P, T]
    self.assertEqual(C4.__args__, (P, T))
    self.assertEqual(C4.__parameters__, (P, T))
