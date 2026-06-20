# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_exception_variations.py
# case: ExceptionTestCase_test_try_finally_no_exception

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    hit_finally = False
    try:
        pass
    finally:
        hit_finally = True
    self.assertTrue(hit_finally)
