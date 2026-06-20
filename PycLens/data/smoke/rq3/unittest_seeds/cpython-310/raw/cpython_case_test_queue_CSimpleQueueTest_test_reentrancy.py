# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_queue.py
# case: CSimpleQueueTest_test_reentrancy

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    q = self.q
    gen = itertools.count()
    N = 10000
    results = []

    class Circular(object):

        def __init__(self):
            self.circular = self

        def __del__(self):
            q.put(next(gen))
    while True:
        o = Circular()
        q.put(next(gen))
        del o
        results.append(q.get())
        if results[-1] >= N:
            break
    self.assertEqual(results, list(range(N + 1)))
