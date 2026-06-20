# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_typing.py
# case: BaseCallableTests_test_errors

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    Callable = self.Callable
    alias = Callable[[int, str], float]
    with self.assertRaisesRegex(TypeError, 'is not a generic class'):
        alias[int]
    P = ParamSpec('P')
    C1 = Callable[P, T]
    with self.assertRaisesRegex(TypeError, 'many arguments for'):
        C1[int, str, str]
    with self.assertRaisesRegex(TypeError, 'few arguments for'):
        C1[int]
