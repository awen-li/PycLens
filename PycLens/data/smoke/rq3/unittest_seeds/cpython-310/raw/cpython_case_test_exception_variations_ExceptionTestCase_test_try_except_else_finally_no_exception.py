# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_exception_variations.py
# case: ExceptionTestCase_test_try_except_else_finally_no_exception

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    hit_except = False
    hit_else = False
    hit_finally = False
    try:
        pass
    except:
        hit_except = True
    else:
        hit_else = True
    finally:
        hit_finally = True
    self.assertFalse(hit_except)
    self.assertTrue(hit_finally)
    self.assertTrue(hit_else)
