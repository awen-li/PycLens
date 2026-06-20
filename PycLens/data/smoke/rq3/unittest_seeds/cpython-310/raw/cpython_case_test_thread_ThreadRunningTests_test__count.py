# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_thread.py
# case: ThreadRunningTests_test__count

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    orig = thread._count()
    mut = thread.allocate_lock()
    mut.acquire()
    started = []

    def task():
        started.append(None)
        mut.acquire()
        mut.release()
    with threading_helper.wait_threads_exit():
        thread.start_new_thread(task, ())
        while not started:
            time.sleep(POLL_SLEEP)
        self.assertEqual(thread._count(), orig + 1)
        mut.release()
        done = []
        wr = weakref.ref(task, lambda _: done.append(None))
        del task
        while not done:
            time.sleep(POLL_SLEEP)
            support.gc_collect()
        self.assertEqual(thread._count(), orig)
