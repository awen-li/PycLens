# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_threading.py
# case: ThreadTests_test_shutdown_locks

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for daemon in (False, True):
        with self.subTest(daemon=daemon):
            event = threading.Event()
            thread = threading.Thread(target=event.wait, daemon=daemon)
            thread.start()
            tstate_lock = thread._tstate_lock
            if not daemon:
                self.assertIn(tstate_lock, threading._shutdown_locks)
            else:
                self.assertNotIn(tstate_lock, threading._shutdown_locks)
            event.set()
            thread.join()
            self.assertNotIn(tstate_lock, threading._shutdown_locks)
