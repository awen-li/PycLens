# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_threading.py
# case: ThreadTests_test_repr_stopped

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
    t = threading.Thread(target=f)
    t.start()
    started.acquire()
    self.assertIn('started', repr(t))
    finish.release()
    LOOKING_FOR = 'stopped'
    for i in range(500):
        if LOOKING_FOR in repr(t):
            break
        time.sleep(0.01)
    self.assertIn(LOOKING_FOR, repr(t))
    t.join()
