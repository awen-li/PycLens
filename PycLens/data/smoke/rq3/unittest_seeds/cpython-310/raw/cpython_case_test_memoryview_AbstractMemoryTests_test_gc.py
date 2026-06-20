# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_memoryview.py
# case: AbstractMemoryTests_test_gc

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for tp in self._types:
        if not isinstance(tp, type):
            continue

        class MyView:

            def __init__(self, base):
                self.m = memoryview(base)

        class MySource(tp):
            pass

        class MyObject:
            pass
        b = MySource(tp(b'abc'))
        m = self._view(b)
        o = MyObject()
        b.m = m
        b.o = o
        wr = weakref.ref(o)
        b = m = o = None
        gc.collect()
        self.assertTrue(wr() is None, wr())
        m = MyView(tp(b'abc'))
        o = MyObject()
        m.x = m
        m.o = o
        wr = weakref.ref(o)
        m = o = None
        gc.collect()
        self.assertTrue(wr() is None, wr())
