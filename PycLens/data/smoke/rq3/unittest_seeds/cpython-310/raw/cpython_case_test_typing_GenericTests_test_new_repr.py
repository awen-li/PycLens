# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_typing.py
# case: GenericTests_test_new_repr

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    T = TypeVar('T')
    U = TypeVar('U', covariant=True)
    S = TypeVar('S')
    self.assertEqual(repr(List), 'typing.List')
    self.assertEqual(repr(List[T]), 'typing.List[~T]')
    self.assertEqual(repr(List[U]), 'typing.List[+U]')
    self.assertEqual(repr(List[S][T][int]), 'typing.List[int]')
    self.assertEqual(repr(List[int]), 'typing.List[int]')
