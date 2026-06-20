# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_typing.py
# case: GenericTests_test_extended_generic_rules_repr

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    T = TypeVar('T')
    self.assertEqual(repr(Union[Tuple, Callable]).replace('typing.', ''), 'Union[Tuple, Callable]')
    self.assertEqual(repr(Union[Tuple, Tuple[int]]).replace('typing.', ''), 'Union[Tuple, Tuple[int]]')
    self.assertEqual(repr(Callable[..., Optional[T]][int]).replace('typing.', ''), 'Callable[..., Optional[int]]')
    self.assertEqual(repr(Callable[[], List[T]][int]).replace('typing.', ''), 'Callable[[], List[int]]')
