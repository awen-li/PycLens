# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_queue.py
# case: BaseSimpleQueueTest_test_order

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    q = self.q
    inputs = list(range(100))
    results = self.run_threads(1, q, inputs, self.feed, self.consume)
    self.assertEqual(results, inputs)
