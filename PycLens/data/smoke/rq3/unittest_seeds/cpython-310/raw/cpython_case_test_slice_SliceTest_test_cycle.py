# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_slice.py
# case: SliceTest_test_cycle

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class myobj:
        pass
    o = myobj()
    o.s = slice(o)
    w = weakref.ref(o)
    o = None
    support.gc_collect()
    self.assertIsNone(w())
