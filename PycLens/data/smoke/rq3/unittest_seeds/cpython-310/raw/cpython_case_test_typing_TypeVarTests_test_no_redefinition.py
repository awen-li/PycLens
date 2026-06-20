# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_typing.py
# case: TypeVarTests_test_no_redefinition

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertNotEqual(TypeVar('T'), TypeVar('T'))
    self.assertNotEqual(TypeVar('T', int, str), TypeVar('T', int, str))
