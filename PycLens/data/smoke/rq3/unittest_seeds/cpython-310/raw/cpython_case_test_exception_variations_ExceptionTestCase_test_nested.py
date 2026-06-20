# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_exception_variations.py
# case: ExceptionTestCase_test_nested

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    hit_finally = False
    hit_inner_except = False
    hit_inner_finally = False
    try:
        try:
            raise Exception('inner exception')
        except:
            hit_inner_except = True
        finally:
            hit_inner_finally = True
    finally:
        hit_finally = True
    self.assertTrue(hit_inner_except)
    self.assertTrue(hit_inner_finally)
    self.assertTrue(hit_finally)
