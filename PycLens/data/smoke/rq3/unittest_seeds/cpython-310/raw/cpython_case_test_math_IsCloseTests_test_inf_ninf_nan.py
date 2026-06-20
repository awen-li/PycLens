# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_math.py
# case: IsCloseTests_test_inf_ninf_nan

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    not_close_examples = [(NAN, NAN), (NAN, 1e-100), (1e-100, NAN), (INF, NAN), (NAN, INF), (INF, NINF), (INF, 1.0), (1.0, INF), (INF, 1e+308), (1e+308, INF)]
    self.assertAllNotClose(not_close_examples, abs_tol=0.999999999999999)
