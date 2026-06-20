# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_typing.py
# case: GenericTests_test_multi_subscr_base

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    T = TypeVar('T')
    U = TypeVar('U')
    V = TypeVar('V')

    class C(List[T][U][V]):
        ...

    class D(C, List[T][U][V]):
        ...
    self.assertEqual(C.__parameters__, (V,))
    self.assertEqual(D.__parameters__, (V,))
    self.assertEqual(C[int].__parameters__, ())
    self.assertEqual(D[int].__parameters__, ())
    self.assertEqual(C[int].__args__, (int,))
    self.assertEqual(D[int].__args__, (int,))
    self.assertEqual(C.__bases__, (list, Generic))
    self.assertEqual(D.__bases__, (C, list, Generic))
    self.assertEqual(C.__orig_bases__, (List[T][U][V],))
    self.assertEqual(D.__orig_bases__, (C, List[T][U][V]))
