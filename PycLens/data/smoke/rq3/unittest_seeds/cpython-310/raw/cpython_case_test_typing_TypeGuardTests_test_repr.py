# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_typing.py
# case: TypeGuardTests_test_repr

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertEqual(repr(TypeGuard), 'typing.TypeGuard')
    cv = TypeGuard[int]
    self.assertEqual(repr(cv), 'typing.TypeGuard[int]')
    cv = TypeGuard[Employee]
    self.assertEqual(repr(cv), 'typing.TypeGuard[%s.Employee]' % __name__)
    cv = TypeGuard[tuple[int]]
    self.assertEqual(repr(cv), 'typing.TypeGuard[tuple[int]]')
