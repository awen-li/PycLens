# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_typing.py
# case: ParamSpecTests_test_paramspec_in_nested_generics

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    T = TypeVar('T')
    P = ParamSpec('P')
    C1 = Callable[P, T]
    G1 = List[C1]
    G2 = list[C1]
    G3 = list[C1] | int
    self.assertEqual(G1.__parameters__, (P, T))
    self.assertEqual(G2.__parameters__, (P, T))
    self.assertEqual(G3.__parameters__, (P, T))
    C = Callable[[int, str], float]
    self.assertEqual(G1[[int, str], float], List[C])
    self.assertEqual(G2[[int, str], float], list[C])
    self.assertEqual(G3[[int, str], float], list[C] | int)
