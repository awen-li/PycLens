# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_queue.py
# case: BaseQueueTestMixin_test_nowait

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    q = self.type2test(QUEUE_SIZE)
    for i in range(QUEUE_SIZE):
        q.put_nowait(1)
    with self.assertRaises(self.queue.Full):
        q.put_nowait(1)
    for i in range(QUEUE_SIZE):
        q.get_nowait()
    with self.assertRaises(self.queue.Empty):
        q.get_nowait()
