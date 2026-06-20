# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_concurrent_futures.py
# case: ThreadPoolExecutorTest_test_saturation

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    executor = self.executor_type(4)

    def acquire_lock(lock):
        lock.acquire()
    sem = threading.Semaphore(0)
    for i in range(15 * executor._max_workers):
        executor.submit(acquire_lock, sem)
    self.assertEqual(len(executor._threads), executor._max_workers)
    for i in range(15 * executor._max_workers):
        sem.release()
    executor.shutdown(wait=True)
