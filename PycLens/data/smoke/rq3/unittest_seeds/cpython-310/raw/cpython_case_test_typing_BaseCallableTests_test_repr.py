# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_typing.py
# case: BaseCallableTests_test_repr

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    Callable = self.Callable
    fullname = f'{Callable.__module__}.Callable'
    ct0 = Callable[[], bool]
    self.assertEqual(repr(ct0), f'{fullname}[[], bool]')
    ct2 = Callable[[str, float], int]
    self.assertEqual(repr(ct2), f'{fullname}[[str, float], int]')
    ctv = Callable[..., str]
    self.assertEqual(repr(ctv), f'{fullname}[..., str]')
    ct3 = Callable[[str, float], list[int]]
    self.assertEqual(repr(ct3), f'{fullname}[[str, float], list[int]]')
