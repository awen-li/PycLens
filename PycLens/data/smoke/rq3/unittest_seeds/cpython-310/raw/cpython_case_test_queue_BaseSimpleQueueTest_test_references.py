# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_queue.py
# case: BaseSimpleQueueTest_test_references

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class C:
        pass
    N = 20
    q = self.q
    for i in range(N):
        q.put(C())
    for i in range(N):
        wr = weakref.ref(q.get())
        gc_collect()
        self.assertIsNone(wr())
