# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_thread.py
# case: ThreadRunningTests_test_nt_and_posix_stack_size

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    try:
        thread.stack_size(4096)
    except ValueError:
        verbose_print('caught expected ValueError setting stack_size(4096)')
    except thread.error:
        self.skipTest('platform does not support changing thread stack size')
    fail_msg = 'stack_size(%d) failed - should succeed'
    for tss in (262144, 1048576, 0):
        thread.stack_size(tss)
        self.assertEqual(thread.stack_size(), tss, fail_msg % tss)
        verbose_print('successfully set stack_size(%d)' % tss)
    for tss in (262144, 1048576):
        verbose_print('trying stack_size = (%d)' % tss)
        self.next_ident = 0
        self.created = 0
        with threading_helper.wait_threads_exit():
            for i in range(NUMTASKS):
                self.newtask()
            verbose_print('waiting for all tasks to complete')
            self.done_mutex.acquire()
            verbose_print('all tasks done')
    thread.stack_size(0)
