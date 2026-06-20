# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_threading.py
# case: ThreadingExceptionTests_test_daemonize_active_thread

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    thread = threading.Thread()
    thread.start()
    self.assertRaises(RuntimeError, setattr, thread, 'daemon', True)
    thread.join()
