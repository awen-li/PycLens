# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_exception_variations.py
# case: ExceptionTestCase_test_try_except_finally

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    hit_except = False
    hit_finally = False
    try:
        raise Exception('yarr!')
    except:
        hit_except = True
    finally:
        hit_finally = True
    self.assertTrue(hit_except)
    self.assertTrue(hit_finally)
