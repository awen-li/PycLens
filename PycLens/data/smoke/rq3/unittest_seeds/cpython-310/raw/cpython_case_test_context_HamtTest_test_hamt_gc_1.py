# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_context.py
# case: HamtTest_test_hamt_gc_1

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    A = HashKey(100, 'A')
    h = hamt()
    h = h.set(0, 0)
    ref = weakref.ref(h)
    a = []
    a.append(a)
    a.append(h)
    b = []
    a.append(b)
    b.append(a)
    h = h.set(A, b)
    del h, a, b
    gc.collect()
    gc.collect()
    gc.collect()
    self.assertIsNone(ref())
