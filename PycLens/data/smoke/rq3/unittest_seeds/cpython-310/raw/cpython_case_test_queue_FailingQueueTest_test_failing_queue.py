# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_queue.py
# case: FailingQueueTest_test_failing_queue

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    q = self.FailingQueue(QUEUE_SIZE)
    self.failing_queue_test(q)
    self.failing_queue_test(q)
