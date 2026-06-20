# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_concurrent_futures.py
# case: ProcessPoolShutdownTest_test_processes_terminate

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def acquire_lock(lock):
        lock.acquire()
    mp_context = self.get_context()
    if mp_context.get_start_method(allow_none=False) == 'fork':
        expected_num_processes = self.worker_count
    else:
        expected_num_processes = 3
    sem = mp_context.Semaphore(0)
    for _ in range(3):
        self.executor.submit(acquire_lock, sem)
    self.assertEqual(len(self.executor._processes), expected_num_processes)
    for _ in range(3):
        sem.release()
    processes = self.executor._processes
    self.executor.shutdown()
    for p in processes.values():
        p.join()
