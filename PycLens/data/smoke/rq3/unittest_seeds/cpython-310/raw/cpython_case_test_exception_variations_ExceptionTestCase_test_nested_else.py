# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_exception_variations.py
# case: ExceptionTestCase_test_nested_else

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    hit_else = False
    hit_finally = False
    hit_except = False
    hit_inner_except = False
    hit_inner_else = False
    try:
        try:
            pass
        except:
            hit_inner_except = True
        else:
            hit_inner_else = True
        raise Exception('outer exception')
    except:
        hit_except = True
    else:
        hit_else = True
    finally:
        hit_finally = True
    self.assertFalse(hit_inner_except)
    self.assertTrue(hit_inner_else)
    self.assertFalse(hit_else)
    self.assertTrue(hit_finally)
    self.assertTrue(hit_except)
