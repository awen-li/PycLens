# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_typing.py
# case: TypeVarTests_test_typevar_subclass_type_error

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    T = TypeVar('T')
    with self.assertRaises(TypeError):
        issubclass(int, T)
    with self.assertRaises(TypeError):
        issubclass(T, int)
