# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_typing.py
# case: TypeVarTests_test_bad_var_substitution

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    T = TypeVar('T')
    for arg in ((), (int, str)):
        with self.subTest(arg=arg):
            with self.assertRaises(TypeError):
                List[T][arg]
            with self.assertRaises(TypeError):
                list[T][arg]
