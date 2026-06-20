# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_typing.py
# case: GenericTests_test_new_repr_complex

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    T = TypeVar('T')
    TS = TypeVar('TS')
    self.assertEqual(repr(typing.Mapping[T, TS][TS, T]), 'typing.Mapping[~TS, ~T]')
    self.assertEqual(repr(List[Tuple[T, TS]][int, T]), 'typing.List[typing.Tuple[int, ~T]]')
    self.assertEqual(repr(List[Tuple[T, T]][List[int]]), 'typing.List[typing.Tuple[typing.List[int], typing.List[int]]]')
