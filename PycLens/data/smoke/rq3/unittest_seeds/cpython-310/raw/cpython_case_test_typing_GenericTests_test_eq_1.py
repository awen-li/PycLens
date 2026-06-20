# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_typing.py
# case: GenericTests_test_eq_1

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertEqual(Generic, Generic)
    self.assertEqual(Generic[T], Generic[T])
    self.assertNotEqual(Generic[KT], Generic[VT])
