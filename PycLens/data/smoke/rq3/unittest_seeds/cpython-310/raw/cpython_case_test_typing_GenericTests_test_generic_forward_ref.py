# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_typing.py
# case: GenericTests_test_generic_forward_ref

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def foobar(x: List[List['CC']]):
        ...

    def foobar2(x: list[list[ForwardRef('CC')]]):
        ...

    def foobar3(x: list[ForwardRef('CC | int')] | int):
        ...

    class CC:
        ...
    self.assertEqual(get_type_hints(foobar, globals(), locals()), {'x': List[List[CC]]})
    self.assertEqual(get_type_hints(foobar2, globals(), locals()), {'x': list[list[CC]]})
    self.assertEqual(get_type_hints(foobar3, globals(), locals()), {'x': list[CC | int] | int})
    T = TypeVar('T')
    AT = Tuple[T, ...]

    def barfoo(x: AT):
        ...
    self.assertIs(get_type_hints(barfoo, globals(), locals())['x'], AT)
    CT = Callable[..., List[T]]

    def barfoo2(x: CT):
        ...
    self.assertIs(get_type_hints(barfoo2, globals(), locals())['x'], CT)
