# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_queue.py
# case: BaseQueueTestMixin_test_negative_timeout_raises_exception

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    q = self.type2test(QUEUE_SIZE)
    with self.assertRaises(ValueError):
        q.put(1, timeout=-1)
    with self.assertRaises(ValueError):
        q.get(1, timeout=-1)
