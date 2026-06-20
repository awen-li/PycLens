# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_threading.py
# case: ThreadTests_test_tstate_lock

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    started = _thread.allocate_lock()
    finish = _thread.allocate_lock()
    started.acquire()
    finish.acquire()

    def f():
        started.release()
        finish.acquire()
        time.sleep(0.01)
    t = threading.Thread(target=f)
    self.assertIs(t._tstate_lock, None)
    t.start()
    started.acquire()
    self.assertTrue(t.is_alive())
    tstate_lock = t._tstate_lock
    self.assertFalse(tstate_lock.acquire(timeout=0), False)
    finish.release()
    self.assertTrue(tstate_lock.acquire(timeout=support.SHORT_TIMEOUT), False)
    self.assertTrue(t.is_alive())
    tstate_lock.release()
    self.assertFalse(t.is_alive())
    self.assertIsNone(t._tstate_lock)
    t.join()
