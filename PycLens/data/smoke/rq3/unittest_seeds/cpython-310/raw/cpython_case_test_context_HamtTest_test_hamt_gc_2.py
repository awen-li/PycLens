# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_context.py
# case: HamtTest_test_hamt_gc_2

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    A = HashKey(100, 'A')
    B = HashKey(101, 'B')
    h = hamt()
    h = h.set(A, 'a')
    h = h.set(A, h)
    ref = weakref.ref(h)
    hi = h.items()
    next(hi)
    del h, hi
    gc.collect()
    gc.collect()
    gc.collect()
    self.assertIsNone(ref())
