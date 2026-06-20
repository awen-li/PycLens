# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_typing.py
# case: BaseCallableTests_test_eq_hash

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    Callable = self.Callable
    C = Callable[[int], int]
    self.assertEqual(C, Callable[[int], int])
    self.assertEqual(len({C, Callable[[int], int]}), 1)
    self.assertNotEqual(C, Callable[[int], str])
    self.assertNotEqual(C, Callable[[str], int])
    self.assertNotEqual(C, Callable[[int, int], int])
    self.assertNotEqual(C, Callable[[], int])
    self.assertNotEqual(C, Callable[..., int])
    self.assertNotEqual(C, Callable)
