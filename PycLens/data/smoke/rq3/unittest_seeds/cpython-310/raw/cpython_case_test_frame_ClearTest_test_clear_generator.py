# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_frame.py
# case: ClearTest_test_clear_generator

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    endly = False

    def g():
        nonlocal endly
        try:
            yield
            self.inner()
        finally:
            endly = True
    gen = g()
    next(gen)
    self.assertFalse(endly)
    gen.gi_frame.clear()
    self.assertTrue(endly)
