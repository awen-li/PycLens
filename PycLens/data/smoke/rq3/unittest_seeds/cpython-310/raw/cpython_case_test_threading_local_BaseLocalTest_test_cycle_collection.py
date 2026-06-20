# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_threading_local.py
# case: BaseLocalTest_test_cycle_collection

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class X:
        pass
    x = X()
    x.local = self._local()
    x.local.x = x
    wr = weakref.ref(x)
    del x
    support.gc_collect()
    self.assertIsNone(wr())
