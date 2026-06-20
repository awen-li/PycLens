# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_compile.py
# case: TestSpecifics_test_sequence_unpacking_error

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    (i, j) = (1, -1) or (-1, 1)
    self.assertEqual(i, 1)
    self.assertEqual(j, -1)
