# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_typing.py
# case: TypedDictTests_test_non_generic_subscript

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class TD(TypedDict):
        a: T
    A = TD[int]
    self.assertEqual(A.__origin__, TD)
    self.assertEqual(A.__parameters__, ())
    self.assertEqual(A.__args__, (int,))
    a = A(a=1)
    self.assertIs(type(a), dict)
    self.assertEqual(a, {'a': 1})
