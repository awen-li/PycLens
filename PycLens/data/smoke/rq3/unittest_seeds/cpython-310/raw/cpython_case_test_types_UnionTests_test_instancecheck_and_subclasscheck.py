# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_types.py
# case: UnionTests_test_instancecheck_and_subclasscheck

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for x in (int | str, typing.Union[int, str]):
        with self.subTest(x=x):
            self.assertIsInstance(1, x)
            self.assertIsInstance(True, x)
            self.assertIsInstance('a', x)
            self.assertNotIsInstance(None, x)
            self.assertTrue(issubclass(int, x))
            self.assertTrue(issubclass(bool, x))
            self.assertTrue(issubclass(str, x))
            self.assertFalse(issubclass(type(None), x))
    for x in (int | None, typing.Union[int, None]):
        with self.subTest(x=x):
            self.assertIsInstance(None, x)
            self.assertTrue(issubclass(type(None), x))
    for x in (int | collections.abc.Mapping, typing.Union[int, collections.abc.Mapping]):
        with self.subTest(x=x):
            self.assertIsInstance({}, x)
            self.assertNotIsInstance((), x)
            self.assertTrue(issubclass(dict, x))
            self.assertFalse(issubclass(list, x))
