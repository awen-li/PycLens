# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_threading.py
# case: ThreadTests_test_limbo_cleanup

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def fail_new_thread(*args):
        raise threading.ThreadError()
    _start_new_thread = threading._start_new_thread
    threading._start_new_thread = fail_new_thread
    try:
        t = threading.Thread(target=lambda : None)
        self.assertRaises(threading.ThreadError, t.start)
        self.assertFalse(t in threading._limbo, 'Failed to cleanup _limbo map on failure of Thread.start().')
    finally:
        threading._start_new_thread = _start_new_thread
