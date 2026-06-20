# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_io.py
# case: MiscIOTest_test_blockingioerror

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class C(str):
        pass
    c = C('')
    b = self.BlockingIOError(1, c)
    c.b = b
    b.c = c
    wr = weakref.ref(c)
    del c, b
    support.gc_collect()
    self.assertIsNone(wr(), wr)
