# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_typing.py
# case: UnionTests_test_repr

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertEqual(repr(Union), 'typing.Union')
    u = Union[Employee, int]
    self.assertEqual(repr(u), 'typing.Union[%s.Employee, int]' % __name__)
    u = Union[int, Employee]
    self.assertEqual(repr(u), 'typing.Union[int, %s.Employee]' % __name__)
    T = TypeVar('T')
    u = Union[T, int][int]
    self.assertEqual(repr(u), repr(int))
    u = Union[List[int], int]
    self.assertEqual(repr(u), 'typing.Union[typing.List[int], int]')
    u = Union[list[int], dict[str, float]]
    self.assertEqual(repr(u), 'typing.Union[list[int], dict[str, float]]')
    u = Union[int | float]
    self.assertEqual(repr(u), 'typing.Union[int, float]')
    u = Union[None, str]
    self.assertEqual(repr(u), 'typing.Optional[str]')
    u = Union[str, None]
    self.assertEqual(repr(u), 'typing.Optional[str]')
    u = Union[None, str, int]
    self.assertEqual(repr(u), 'typing.Union[NoneType, str, int]')
    u = Optional[str]
    self.assertEqual(repr(u), 'typing.Optional[str]')
