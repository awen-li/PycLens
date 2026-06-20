# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_typing.py
# case: TypeVarTests_test_union_unique

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    X = TypeVar('X')
    Y = TypeVar('Y')
    self.assertNotEqual(X, Y)
    self.assertEqual(Union[X], X)
    self.assertNotEqual(Union[X], Union[X, Y])
    self.assertEqual(Union[X, X], X)
    self.assertNotEqual(Union[X, int], Union[X])
    self.assertNotEqual(Union[X, int], Union[int])
    self.assertEqual(Union[X, int].__args__, (X, int))
    self.assertEqual(Union[X, int].__parameters__, (X,))
    self.assertIs(Union[X, int].__origin__, Union)
