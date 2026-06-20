# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_typing.py
# case: FinalTests_test_repr

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertEqual(repr(Final), 'typing.Final')
    cv = Final[int]
    self.assertEqual(repr(cv), 'typing.Final[int]')
    cv = Final[Employee]
    self.assertEqual(repr(cv), 'typing.Final[%s.Employee]' % __name__)
    cv = Final[tuple[int]]
    self.assertEqual(repr(cv), 'typing.Final[tuple[int]]')
