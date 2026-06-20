# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_typing.py
# case: GetUtilitiesTestCase_test_get_args

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    T = TypeVar('T')

    class C(Generic[T]):
        pass
    self.assertEqual(get_args(C[int]), (int,))
    self.assertEqual(get_args(C[T]), (T,))
    self.assertEqual(get_args(int), ())
    self.assertEqual(get_args(ClassVar[int]), (int,))
    self.assertEqual(get_args(Union[int, str]), (int, str))
    self.assertEqual(get_args(Literal[42, 43]), (42, 43))
    self.assertEqual(get_args(Final[List[int]]), (List[int],))
    self.assertEqual(get_args(Union[int, Tuple[T, int]][str]), (int, Tuple[str, int]))
    self.assertEqual(get_args(typing.Dict[int, Tuple[T, T]][Optional[int]]), (int, Tuple[Optional[int], Optional[int]]))
    self.assertEqual(get_args(Callable[[], T][int]), ([], int))
    self.assertEqual(get_args(Callable[..., int]), (..., int))
    self.assertEqual(get_args(Union[int, Callable[[Tuple[T, ...]], str]]), (int, Callable[[Tuple[T, ...]], str]))
    self.assertEqual(get_args(Tuple[int, ...]), (int, ...))
    self.assertEqual(get_args(Tuple[()]), ((),))
    self.assertEqual(get_args(Annotated[T, 'one', 2, ['three']]), (T, 'one', 2, ['three']))
    self.assertEqual(get_args(List), ())
    self.assertEqual(get_args(Tuple), ())
    self.assertEqual(get_args(Callable), ())
    self.assertEqual(get_args(list[int]), (int,))
    self.assertEqual(get_args(list), ())
    self.assertEqual(get_args(collections.abc.Callable[[int], str]), ([int], str))
    self.assertEqual(get_args(collections.abc.Callable[..., str]), (..., str))
    self.assertEqual(get_args(collections.abc.Callable[[], str]), ([], str))
    self.assertEqual(get_args(collections.abc.Callable[[int], str]), get_args(Callable[[int], str]))
    P = ParamSpec('P')
    self.assertEqual(get_args(Callable[P, int]), (P, int))
    self.assertEqual(get_args(Callable[Concatenate[int, P], int]), (Concatenate[int, P], int))
    self.assertEqual(get_args(list | str), (list, str))
