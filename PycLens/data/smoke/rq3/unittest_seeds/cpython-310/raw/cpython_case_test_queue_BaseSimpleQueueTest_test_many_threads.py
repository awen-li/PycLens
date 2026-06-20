# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_queue.py
# case: BaseSimpleQueueTest_test_many_threads

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    N = 50
    q = self.q
    inputs = list(range(10000))
    results = self.run_threads(N, q, inputs, self.feed, self.consume)
    self.assertEqual(sorted(results), inputs)
