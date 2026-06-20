# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_typing.py
# case: ParamSpecTests_test_paramspec_gets_copied

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    P = ParamSpec('P')
    P2 = ParamSpec('P2')
    C1 = Callable[P, int]
    self.assertEqual(C1.__parameters__, (P,))
    self.assertEqual(C1[P2].__parameters__, (P2,))
    self.assertEqual(C1[str].__parameters__, ())
    self.assertEqual(C1[str, T].__parameters__, (T,))
    self.assertEqual(C1[Concatenate[str, P2]].__parameters__, (P2,))
    self.assertEqual(C1[Concatenate[T, P2]].__parameters__, (T, P2))
    self.assertEqual(C1[...].__parameters__, ())
    C2 = Callable[Concatenate[str, P], int]
    self.assertEqual(C2.__parameters__, (P,))
    self.assertEqual(C2[P2].__parameters__, (P2,))
    self.assertEqual(C2[str].__parameters__, ())
    self.assertEqual(C2[str, T].__parameters__, (T,))
    self.assertEqual(C2[Concatenate[str, P2]].__parameters__, (P2,))
    self.assertEqual(C2[Concatenate[T, P2]].__parameters__, (T, P2))
