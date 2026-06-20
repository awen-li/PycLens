# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_typing.py
# case: BaseCallableTests_test_paramspec

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    Callable = self.Callable
    fullname = f'{Callable.__module__}.Callable'
    P = ParamSpec('P')
    P2 = ParamSpec('P2')
    C1 = Callable[P, T]
    self.assertEqual(C1[[int], str], Callable[[int], str])
    self.assertEqual(C1[[int, str], str], Callable[[int, str], str])
    self.assertEqual(C1[[], str], Callable[[], str])
    self.assertEqual(C1[..., str], Callable[..., str])
    self.assertEqual(C1[P2, str], Callable[P2, str])
    self.assertEqual(C1[Concatenate[int, P2], str], Callable[Concatenate[int, P2], str])
    self.assertEqual(repr(C1), f'{fullname}[~P, ~T]')
    self.assertEqual(repr(C1[[int, str], str]), f'{fullname}[[int, str], str]')
    with self.assertRaises(TypeError):
        C1[int, str]
    C2 = Callable[P, int]
    self.assertEqual(C2[[int]], Callable[[int], int])
    self.assertEqual(C2[[int, str]], Callable[[int, str], int])
    self.assertEqual(C2[[]], Callable[[], int])
    self.assertEqual(C2[...], Callable[..., int])
    self.assertEqual(C2[P2], Callable[P2, int])
    self.assertEqual(C2[Concatenate[int, P2]], Callable[Concatenate[int, P2], int])
    self.assertEqual(C2[int], Callable[[int], int])
    self.assertEqual(C2[int, str], Callable[[int, str], int])
    self.assertEqual(repr(C2), f'{fullname}[~P, int]')
    self.assertEqual(repr(C2[int, str]), f'{fullname}[[int, str], int]')
