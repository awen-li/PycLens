# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_typing.py
# case: GetTypeHintTests_test_get_type_hints_annotated

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def foobar(x: List['X']):
        ...
    X = Annotated[int, (1, 10)]
    self.assertEqual(get_type_hints(foobar, globals(), locals()), {'x': List[int]})
    self.assertEqual(get_type_hints(foobar, globals(), locals(), include_extras=True), {'x': List[Annotated[int, (1, 10)]]})

    def foobar(x: list[ForwardRef('X')]):
        ...
    X = Annotated[int, (1, 10)]
    self.assertEqual(get_type_hints(foobar, globals(), locals()), {'x': list[int]})
    self.assertEqual(get_type_hints(foobar, globals(), locals(), include_extras=True), {'x': list[Annotated[int, (1, 10)]]})
    BA = Tuple[Annotated[T, (1, 0)], ...]

    def barfoo(x: BA):
        ...
    self.assertEqual(get_type_hints(barfoo, globals(), locals())['x'], Tuple[T, ...])
    self.assertIs(get_type_hints(barfoo, globals(), locals(), include_extras=True)['x'], BA)
    BA = tuple[Annotated[T, (1, 0)], ...]

    def barfoo(x: BA):
        ...
    self.assertEqual(get_type_hints(barfoo, globals(), locals())['x'], tuple[T, ...])
    self.assertIs(get_type_hints(barfoo, globals(), locals(), include_extras=True)['x'], BA)

    def barfoo2(x: typing.Callable[..., Annotated[List[T], 'const']], y: typing.Union[int, Annotated[T, 'mutable']]):
        ...
    self.assertEqual(get_type_hints(barfoo2, globals(), locals()), {'x': typing.Callable[..., List[T]], 'y': typing.Union[int, T]})
    BA2 = typing.Callable[..., List[T]]

    def barfoo3(x: BA2):
        ...
    self.assertIs(get_type_hints(barfoo3, globals(), locals(), include_extras=True)['x'], BA2)
    BA3 = typing.Annotated[int | float, 'const']

    def barfoo4(x: BA3):
        ...
    self.assertEqual(get_type_hints(barfoo4, globals(), locals()), {'x': int | float})
    self.assertEqual(get_type_hints(barfoo4, globals(), locals(), include_extras=True), {'x': typing.Annotated[int | float, 'const']})
