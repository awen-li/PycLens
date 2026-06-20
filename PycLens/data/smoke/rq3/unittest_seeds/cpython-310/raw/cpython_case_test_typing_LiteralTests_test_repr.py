# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_typing.py
# case: LiteralTests_test_repr

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertEqual(repr(Literal[1]), 'typing.Literal[1]')
    self.assertEqual(repr(Literal[1, True, 'foo']), "typing.Literal[1, True, 'foo']")
    self.assertEqual(repr(Literal[int]), 'typing.Literal[int]')
    self.assertEqual(repr(Literal), 'typing.Literal')
    self.assertEqual(repr(Literal[None]), 'typing.Literal[None]')
    self.assertEqual(repr(Literal[1, 2, 3, 3]), 'typing.Literal[1, 2, 3]')
