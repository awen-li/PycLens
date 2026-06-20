# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_queue.py
# case: BaseQueueTestMixin_test_shrinking_queue

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    q = self.type2test(3)
    q.put(1)
    q.put(2)
    q.put(3)
    with self.assertRaises(self.queue.Full):
        q.put_nowait(4)
    self.assertEqual(q.qsize(), 3)
    q.maxsize = 2
    with self.assertRaises(self.queue.Full):
        q.put_nowait(4)
