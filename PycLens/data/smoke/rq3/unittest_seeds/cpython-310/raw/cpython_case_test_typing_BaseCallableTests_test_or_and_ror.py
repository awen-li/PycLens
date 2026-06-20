# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_typing.py
# case: BaseCallableTests_test_or_and_ror

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    Callable = self.Callable
    self.assertEqual(Callable | Tuple, Union[Callable, Tuple])
    self.assertEqual(Tuple | Callable, Union[Tuple, Callable])
