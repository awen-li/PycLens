# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_typing.py
# case: BaseCallableTests_test_var_substitution

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    Callable = self.Callable
    fullname = f'{Callable.__module__}.Callable'
    C1 = Callable[[int, T], T]
    C2 = Callable[[KT, T], VT]
    C3 = Callable[..., T]
    self.assertEqual(C1[str], Callable[[int, str], str])
    if Callable is typing.Callable:
        self.assertEqual(C1[None], Callable[[int, type(None)], type(None)])
    self.assertEqual(C2[int, float, str], Callable[[int, float], str])
    self.assertEqual(C3[int], Callable[..., int])
    self.assertEqual(C3[NoReturn], Callable[..., NoReturn])
    C4 = C2[int, VT, str]
    self.assertEqual(repr(C4), f'{fullname}[[int, ~VT], str]')
    self.assertEqual(repr(C4[dict]), f'{fullname}[[int, dict], str]')
    self.assertEqual(C4[dict], Callable[[int, dict], str])
    C5 = Callable[[typing.List[T], tuple[KT, T], VT], int]
    self.assertEqual(C5[int, str, float], Callable[[typing.List[int], tuple[str, int], float], int])
