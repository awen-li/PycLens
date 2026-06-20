# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_types.py
# case: UnionTests_test_union_args

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def check(arg, expected):
        clear_typing_caches()
        self.assertEqual(arg.__args__, expected)
    check(int | str, (int, str))
    check(int | str | list, (int, str, list))
    check(int | (str | list), (int, str, list))
    check(int | str | int, (int, str))
    check(int | (str | int), (int, str))
    check(int | str | (str | int), (int, str))
    check(typing.Union[int, str] | list, (int, str, list))
    check(int | typing.Union[str, list], (int, str, list))
    check(int | str | (list | int), (int, str, list))
    check(int | str | typing.Union[list, int], (int, str, list))
    check(typing.Union[int, str] | (list | int), (int, str, list))
    check(str | int | (int | list), (str, int, list))
    check(str | int | typing.Union[int, list], (str, int, list))
    check(typing.Union[str, int] | (int | list), (str, int, list))
    check(int | type(None), (int, type(None)))
    check(type(None) | int, (type(None), int))
    args = (int, list[int], typing.List[int], typing.Tuple[int, int], typing.Callable[[int], int], typing.Hashable, typing.TypeVar('T'))
    for x in args:
        with self.subTest(x):
            check(x | None, (x, type(None)))
            check(None | x, (type(None), x))
