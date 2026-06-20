# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_typing.py
# case: ParamSpecTests_test_bad_var_substitution

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    T = TypeVar('T')
    P = ParamSpec('P')
    bad_args = (42, int, None, T, int | str, Union[int, str])
    for arg in bad_args:
        with self.subTest(arg=arg):
            with self.assertRaises(TypeError):
                typing.Callable[P, T][arg, str]
            with self.assertRaises(TypeError):
                collections.abc.Callable[P, T][arg, str]
