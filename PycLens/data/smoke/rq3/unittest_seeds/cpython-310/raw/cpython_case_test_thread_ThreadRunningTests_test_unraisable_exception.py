# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_thread.py
# case: ThreadRunningTests_test_unraisable_exception

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def task():
        started.release()
        raise ValueError('task failed')
    started = thread.allocate_lock()
    with support.catch_unraisable_exception() as cm:
        with threading_helper.wait_threads_exit():
            started.acquire()
            thread.start_new_thread(task, ())
            started.acquire()
        self.assertEqual(str(cm.unraisable.exc_value), 'task failed')
        self.assertIs(cm.unraisable.object, task)
        self.assertEqual(cm.unraisable.err_msg, 'Exception ignored in thread started by')
        self.assertIsNotNone(cm.unraisable.exc_traceback)
