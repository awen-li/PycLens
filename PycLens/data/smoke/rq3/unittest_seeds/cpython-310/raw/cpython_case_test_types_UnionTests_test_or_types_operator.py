# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_types.py
# case: UnionTests_test_or_types_operator

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertEqual(int | str, typing.Union[int, str])
    self.assertNotEqual(int | list, typing.Union[int, str])
    self.assertEqual(str | int, typing.Union[int, str])
    self.assertEqual(int | None, typing.Union[int, None])
    self.assertEqual(None | int, typing.Union[int, None])
    self.assertEqual(int | type(None), int | None)
    self.assertEqual(type(None) | int, None | int)
    self.assertEqual(int | str | list, typing.Union[int, str, list])
    self.assertEqual(int | (str | list), typing.Union[int, str, list])
    self.assertEqual(str | (int | list), typing.Union[int, str, list])
    self.assertEqual(typing.List | typing.Tuple, typing.Union[typing.List, typing.Tuple])
    self.assertEqual(typing.List[int] | typing.Tuple[int], typing.Union[typing.List[int], typing.Tuple[int]])
    self.assertEqual(typing.List[int] | None, typing.Union[typing.List[int], None])
    self.assertEqual(None | typing.List[int], typing.Union[None, typing.List[int]])
    self.assertEqual(str | float | int | complex | int, int | str | (float | complex))
    self.assertEqual(typing.Union[str, int, typing.List[int]], str | int | typing.List[int])
    self.assertIs(int | int, int)
    self.assertEqual(BaseException | bool | bytes | complex | float | int | list | map | set, typing.Union[BaseException, bool, bytes, complex, float, int, list, map, set])
    with self.assertRaises(TypeError):
        int | 3
    with self.assertRaises(TypeError):
        3 | int
    with self.assertRaises(TypeError):
        Example() | int
    x = int | str
    self.assertEqual(x, int | str)
    self.assertEqual(x, str | int)
    self.assertNotEqual(x, {})
    with self.assertRaises(TypeError):
        x < x
    with self.assertRaises(TypeError):
        x <= x
    y = typing.Union[str, int]
    with self.assertRaises(TypeError):
        x < y
    y = int | bool
    with self.assertRaises(TypeError):
        x < y
    y = typing.Union[str, int]
    y.__args__ = [str, int]
    self.assertEqual(x, y)
