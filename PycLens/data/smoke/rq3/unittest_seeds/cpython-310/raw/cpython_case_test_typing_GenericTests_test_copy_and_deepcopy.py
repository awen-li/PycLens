# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_typing.py
# case: GenericTests_test_copy_and_deepcopy

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    T = TypeVar('T')

    class Node(Generic[T]):
        ...
    things = [Union[T, int], Tuple[T, int], Tuple[()], Callable[..., T], Callable[[int], int], Tuple[Any, Any], Node[T], Node[int], Node[Any], typing.Iterable[T], typing.Iterable[Any], typing.Iterable[int], typing.Dict[int, str], typing.Dict[T, Any], ClassVar[int], ClassVar[List[T]], Tuple['T', 'T'], Union['T', int], List['T'], typing.Mapping['T', int]]
    for t in things + [Any]:
        self.assertEqual(t, copy(t))
        self.assertEqual(t, deepcopy(t))
