# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_thread.py
# case: BarrierTest_test_barrier

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with threading_helper.wait_threads_exit():
        self.bar = Barrier(NUMTASKS)
        self.running = NUMTASKS
        for i in range(NUMTASKS):
            thread.start_new_thread(self.task2, (i,))
        verbose_print('waiting for tasks to end')
        self.done_mutex.acquire()
        verbose_print('tasks done')
