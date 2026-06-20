# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_typing.py
# case: GenericTests_test_weakref_all

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    T = TypeVar('T')
    things = [Any, Union[T, int], Callable[..., T], Tuple[Any, Any], Optional[List[int]], typing.Mapping[int, str], typing.re.Match[bytes], typing.Iterable['whatever']]
    for t in things:
        self.assertEqual(weakref.ref(t)(), t)
