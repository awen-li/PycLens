# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_queue.py
# case: BaseSimpleQueueTest_test_basic

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    q = self.q
    self.assertTrue(q.empty())
    self.assertEqual(q.qsize(), 0)
    q.put(1)
    self.assertFalse(q.empty())
    self.assertEqual(q.qsize(), 1)
    q.put(2)
    q.put_nowait(3)
    q.put(4)
    self.assertFalse(q.empty())
    self.assertEqual(q.qsize(), 4)
    self.assertEqual(q.get(), 1)
    self.assertEqual(q.qsize(), 3)
    self.assertEqual(q.get_nowait(), 2)
    self.assertEqual(q.qsize(), 2)
    self.assertEqual(q.get(block=False), 3)
    self.assertFalse(q.empty())
    self.assertEqual(q.qsize(), 1)
    self.assertEqual(q.get(timeout=0.1), 4)
    self.assertTrue(q.empty())
    self.assertEqual(q.qsize(), 0)
    with self.assertRaises(self.queue.Empty):
        q.get(block=False)
    with self.assertRaises(self.queue.Empty):
        q.get(timeout=0.001)
    with self.assertRaises(self.queue.Empty):
        q.get_nowait()
    self.assertTrue(q.empty())
    self.assertEqual(q.qsize(), 0)
