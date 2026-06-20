# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_typing.py
# case: TupleTests_test_repr

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertEqual(repr(Tuple), 'typing.Tuple')
    self.assertEqual(repr(Tuple[()]), 'typing.Tuple[()]')
    self.assertEqual(repr(Tuple[int, float]), 'typing.Tuple[int, float]')
    self.assertEqual(repr(Tuple[int, ...]), 'typing.Tuple[int, ...]')
    self.assertEqual(repr(Tuple[list[int]]), 'typing.Tuple[list[int]]')
