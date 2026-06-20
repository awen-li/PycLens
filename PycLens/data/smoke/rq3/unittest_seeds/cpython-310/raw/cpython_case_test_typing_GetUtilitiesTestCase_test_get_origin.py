# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_typing.py
# case: GetUtilitiesTestCase_test_get_origin

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    T = TypeVar('T')
    P = ParamSpec('P')

    class C(Generic[T]):
        pass
    self.assertIs(get_origin(C[int]), C)
    self.assertIs(get_origin(C[T]), C)
    self.assertIs(get_origin(int), None)
    self.assertIs(get_origin(ClassVar[int]), ClassVar)
    self.assertIs(get_origin(Union[int, str]), Union)
    self.assertIs(get_origin(Literal[42, 43]), Literal)
    self.assertIs(get_origin(Final[List[int]]), Final)
    self.assertIs(get_origin(Generic), Generic)
    self.assertIs(get_origin(Generic[T]), Generic)
    self.assertIs(get_origin(List[Tuple[T, T]][int]), list)
    self.assertIs(get_origin(Annotated[T, 'thing']), Annotated)
    self.assertIs(get_origin(List), list)
    self.assertIs(get_origin(Tuple), tuple)
    self.assertIs(get_origin(Callable), collections.abc.Callable)
    self.assertIs(get_origin(list[int]), list)
    self.assertIs(get_origin(list), None)
    self.assertIs(get_origin(list | str), types.UnionType)
    self.assertIs(get_origin(P.args), P)
    self.assertIs(get_origin(P.kwargs), P)
