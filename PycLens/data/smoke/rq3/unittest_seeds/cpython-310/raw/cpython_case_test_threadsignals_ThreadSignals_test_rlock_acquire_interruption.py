# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_threadsignals.py
# case: ThreadSignals_test_rlock_acquire_interruption

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    oldalrm = signal.signal(signal.SIGALRM, self.alarm_interrupt)
    try:
        rlock = thread.RLock()

        def other_thread():
            rlock.acquire()
        with threading_helper.wait_threads_exit():
            thread.start_new_thread(other_thread, ())
            while rlock.acquire(blocking=False):
                rlock.release()
                time.sleep(0.01)
            signal.alarm(1)
            t1 = time.monotonic()
            self.assertRaises(KeyboardInterrupt, rlock.acquire, timeout=5)
            dt = time.monotonic() - t1
            self.assertLess(dt, 3.0)
    finally:
        signal.alarm(0)
        signal.signal(signal.SIGALRM, oldalrm)
