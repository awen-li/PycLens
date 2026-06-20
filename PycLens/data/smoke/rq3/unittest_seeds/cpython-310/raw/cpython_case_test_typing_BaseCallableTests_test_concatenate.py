# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_typing.py
# case: BaseCallableTests_test_concatenate

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    Callable = self.Callable
    fullname = f'{Callable.__module__}.Callable'
    T = TypeVar('T')
    P = ParamSpec('P')
    P2 = ParamSpec('P2')
    C = Callable[Concatenate[int, P], T]
    self.assertEqual(repr(C), f'{fullname}[typing.Concatenate[int, ~P], ~T]')
    self.assertEqual(C[P2, int], Callable[Concatenate[int, P2], int])
    self.assertEqual(C[[str, float], int], Callable[[int, str, float], int])
    self.assertEqual(C[[], int], Callable[[int], int])
    self.assertEqual(C[Concatenate[str, P2], int], Callable[Concatenate[int, str, P2], int])
    with self.assertRaises(TypeError):
        C[..., int]
    C = Callable[Concatenate[int, P], int]
    self.assertEqual(repr(C), f'{fullname}[typing.Concatenate[int, ~P], int]')
    self.assertEqual(C[P2], Callable[Concatenate[int, P2], int])
    self.assertEqual(C[[str, float]], Callable[[int, str, float], int])
    self.assertEqual(C[str, float], Callable[[int, str, float], int])
    self.assertEqual(C[[]], Callable[[int], int])
    self.assertEqual(C[Concatenate[str, P2]], Callable[Concatenate[int, str, P2], int])
    with self.assertRaises(TypeError):
        C[...]
