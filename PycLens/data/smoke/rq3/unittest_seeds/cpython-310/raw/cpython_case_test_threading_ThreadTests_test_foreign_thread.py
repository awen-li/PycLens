# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_threading.py
# case: ThreadTests_test_foreign_thread

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def f(mutex):
        threading.current_thread()
        mutex.release()
    mutex = threading.Lock()
    mutex.acquire()
    with threading_helper.wait_threads_exit():
        tid = _thread.start_new_thread(f, (mutex,))
        mutex.acquire()
    self.assertIn(tid, threading._active)
    self.assertIsInstance(threading._active[tid], threading._DummyThread)
    self.assertTrue(threading._active[tid].is_alive())
    self.assertRegex(repr(threading._active[tid]), '_DummyThread')
    del threading._active[tid]
