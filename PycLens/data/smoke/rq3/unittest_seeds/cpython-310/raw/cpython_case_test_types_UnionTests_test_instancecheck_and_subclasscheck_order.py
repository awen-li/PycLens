# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_types.py
# case: UnionTests_test_instancecheck_and_subclasscheck_order

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    T = typing.TypeVar('T')
    will_resolve = (int | T, typing.Union[int, T])
    for x in will_resolve:
        with self.subTest(x=x):
            self.assertIsInstance(1, x)
            self.assertTrue(issubclass(int, x))
    wont_resolve = (T | int, typing.Union[T, int])
    for x in wont_resolve:
        with self.subTest(x=x):
            with self.assertRaises(TypeError):
                issubclass(int, x)
            with self.assertRaises(TypeError):
                isinstance(1, x)
    for x in (*will_resolve, *wont_resolve):
        with self.subTest(x=x):
            with self.assertRaises(TypeError):
                issubclass(object, x)
            with self.assertRaises(TypeError):
                isinstance(object(), x)
