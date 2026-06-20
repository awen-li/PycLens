# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_sched.py
# case: TestCase_test_enter_concurrent

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    q = queue.Queue()
    fun = q.put
    timer = Timer()
    scheduler = sched.scheduler(timer.time, timer.sleep)
    scheduler.enter(1, 1, fun, (1,))
    scheduler.enter(3, 1, fun, (3,))
    t = threading.Thread(target=scheduler.run)
    t.start()
    timer.advance(1)
    self.assertEqual(q.get(timeout=TIMEOUT), 1)
    self.assertTrue(q.empty())
    for x in [4, 5, 2]:
        z = scheduler.enter(x - 1, 1, fun, (x,))
    timer.advance(2)
    self.assertEqual(q.get(timeout=TIMEOUT), 2)
    self.assertEqual(q.get(timeout=TIMEOUT), 3)
    self.assertTrue(q.empty())
    timer.advance(1)
    self.assertEqual(q.get(timeout=TIMEOUT), 4)
    self.assertTrue(q.empty())
    timer.advance(1)
    self.assertEqual(q.get(timeout=TIMEOUT), 5)
    self.assertTrue(q.empty())
    timer.advance(1000)
    threading_helper.join_thread(t)
    self.assertTrue(q.empty())
    self.assertEqual(timer.time(), 5)
