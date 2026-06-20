# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_typing.py
# case: TupleTests_test_equality

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertEqual(Tuple[int], Tuple[int])
    self.assertEqual(Tuple[int, ...], Tuple[int, ...])
    self.assertNotEqual(Tuple[int], Tuple[int, int])
    self.assertNotEqual(Tuple[int], Tuple[int, ...])
