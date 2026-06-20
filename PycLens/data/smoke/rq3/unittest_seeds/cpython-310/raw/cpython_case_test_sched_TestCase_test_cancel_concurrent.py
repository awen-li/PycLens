# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_sched.py
# case: TestCase_test_cancel_concurrent

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    q = queue.Queue()
    fun = q.put
    timer = Timer()
    scheduler = sched.scheduler(timer.time, timer.sleep)
    now = timer.time()
    event1 = scheduler.enterabs(now + 1, 1, fun, (1,))
    event2 = scheduler.enterabs(now + 2, 1, fun, (2,))
    event4 = scheduler.enterabs(now + 4, 1, fun, (4,))
    event5 = scheduler.enterabs(now + 5, 1, fun, (5,))
    event3 = scheduler.enterabs(now + 3, 1, fun, (3,))
    t = threading.Thread(target=scheduler.run)
    t.start()
    timer.advance(1)
    self.assertEqual(q.get(timeout=TIMEOUT), 1)
    self.assertTrue(q.empty())
    scheduler.cancel(event2)
    scheduler.cancel(event5)
    timer.advance(1)
    self.assertTrue(q.empty())
    timer.advance(1)
    self.assertEqual(q.get(timeout=TIMEOUT), 3)
    self.assertTrue(q.empty())
    timer.advance(1)
    self.assertEqual(q.get(timeout=TIMEOUT), 4)
    self.assertTrue(q.empty())
    timer.advance(1000)
    threading_helper.join_thread(t)
    self.assertTrue(q.empty())
    self.assertEqual(timer.time(), 4)
