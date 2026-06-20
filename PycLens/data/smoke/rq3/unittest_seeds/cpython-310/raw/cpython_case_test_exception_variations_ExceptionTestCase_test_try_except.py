# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_exception_variations.py
# case: ExceptionTestCase_test_try_except

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    hit_except = False
    try:
        raise Exception('ahoy!')
    except:
        hit_except = True
    self.assertTrue(hit_except)
