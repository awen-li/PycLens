# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_typing.py
# case: BaseCallableTests_test_type_subst_error

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    Callable = self.Callable
    P = ParamSpec('P')
    T = TypeVar('T')
    pat = 'Expected a list of types, an ellipsis, ParamSpec, or Concatenate.'
    with self.assertRaisesRegex(TypeError, pat):
        Callable[P, T][0, int]
