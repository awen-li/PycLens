# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_frame.py
# case: ClearTest_test_clear_locals

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class C:
        pass
    c = C()
    wr = weakref.ref(c)
    exc = self.outer(c=c)
    del c
    support.gc_collect()
    self.assertIsNot(None, wr())
    self.clear_traceback_frames(exc.__traceback__)
    support.gc_collect()
    self.assertIs(None, wr())
