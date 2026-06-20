# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_typing.py
# case: TypeVarTests_test_repr

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertEqual(repr(T), '~T')
    self.assertEqual(repr(KT), '~KT')
    self.assertEqual(repr(VT), '~VT')
    self.assertEqual(repr(AnyStr), '~AnyStr')
    T_co = TypeVar('T_co', covariant=True)
    self.assertEqual(repr(T_co), '+T_co')
    T_contra = TypeVar('T_contra', contravariant=True)
    self.assertEqual(repr(T_contra), '-T_contra')
