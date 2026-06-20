# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_typing.py
# case: ClassVarTests_test_repr

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertEqual(repr(ClassVar), 'typing.ClassVar')
    cv = ClassVar[int]
    self.assertEqual(repr(cv), 'typing.ClassVar[int]')
    cv = ClassVar[Employee]
    self.assertEqual(repr(cv), 'typing.ClassVar[%s.Employee]' % __name__)
