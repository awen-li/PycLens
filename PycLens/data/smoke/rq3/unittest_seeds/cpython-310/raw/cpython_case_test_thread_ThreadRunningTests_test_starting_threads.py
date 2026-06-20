# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_thread.py
# case: ThreadRunningTests_test_starting_threads

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with threading_helper.wait_threads_exit():
        for i in range(NUMTASKS):
            self.newtask()
        verbose_print('waiting for tasks to complete...')
        self.done_mutex.acquire()
        verbose_print('all tasks done')
