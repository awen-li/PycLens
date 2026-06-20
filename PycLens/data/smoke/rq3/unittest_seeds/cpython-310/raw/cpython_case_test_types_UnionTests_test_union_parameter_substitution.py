# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_types.py
# case: UnionTests_test_union_parameter_substitution

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def eq(actual, expected, typed=True):
        self.assertEqual(actual, expected)
        if typed:
            self.assertIs(type(actual), type(expected))
    T = typing.TypeVar('T')
    S = typing.TypeVar('S')
    NT = typing.NewType('NT', str)
    x = int | T | bytes
    eq(x[str], int | str | bytes, typed=False)
    eq(x[list[int]], int | list[int] | bytes, typed=False)
    eq(x[typing.List], int | typing.List | bytes)
    eq(x[typing.List[int]], int | typing.List[int] | bytes)
    eq(x[typing.Hashable], int | typing.Hashable | bytes)
    eq(x[collections.abc.Hashable], int | collections.abc.Hashable | bytes, typed=False)
    eq(x[typing.Callable[[int], str]], int | typing.Callable[[int], str] | bytes)
    eq(x[collections.abc.Callable[[int], str]], int | collections.abc.Callable[[int], str] | bytes, typed=False)
    eq(x[typing.Tuple[int, str]], int | typing.Tuple[int, str] | bytes)
    eq(x[typing.Literal['none']], int | typing.Literal['none'] | bytes)
    eq(x[str | list], int | str | list | bytes, typed=False)
    eq(x[typing.Union[str, list]], typing.Union[int, str, list, bytes])
    eq(x[str | int], int | str | bytes, typed=False)
    eq(x[typing.Union[str, int]], typing.Union[int, str, bytes])
    eq(x[NT], int | NT | bytes)
    eq(x[S], int | S | bytes)
