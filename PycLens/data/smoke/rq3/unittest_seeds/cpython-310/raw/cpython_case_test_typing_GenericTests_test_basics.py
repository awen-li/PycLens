# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_typing.py
# case: GenericTests_test_basics

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    X = SimpleMapping[str, Any]
    self.assertEqual(X.__parameters__, ())
    with self.assertRaises(TypeError):
        X[str]
    with self.assertRaises(TypeError):
        X[str, str]
    Y = SimpleMapping[XK, str]
    self.assertEqual(Y.__parameters__, (XK,))
    Y[str]
    with self.assertRaises(TypeError):
        Y[str, str]
    SM1 = SimpleMapping[str, int]
    with self.assertRaises(TypeError):
        issubclass(SM1, SimpleMapping)
    self.assertIsInstance(SM1(), SimpleMapping)
    T = TypeVar('T')
    self.assertEqual(List[list[T] | float].__parameters__, (T,))
