# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_concurrent_futures.py
# case: ThreadPoolShutdownTest_test_threads_terminate

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def acquire_lock(lock):
        lock.acquire()
    sem = threading.Semaphore(0)
    for i in range(3):
        self.executor.submit(acquire_lock, sem)
    self.assertEqual(len(self.executor._threads), 3)
    for i in range(3):
        sem.release()
    self.executor.shutdown()
    for t in self.executor._threads:
        t.join()
