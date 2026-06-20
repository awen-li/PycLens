# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_math.py
# case: IsCloseTests_test_integers

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    integer_examples = [(100000001, 100000000), (123456789, 123456788)]
    self.assertAllClose(integer_examples, rel_tol=1e-08)
    self.assertAllNotClose(integer_examples, rel_tol=1e-09)
