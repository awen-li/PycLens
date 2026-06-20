# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_concurrent_futures.py
# case: ProcessPoolExecutorTest_test_saturation

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    executor = self.executor
    mp_context = self.get_context()
    sem = mp_context.Semaphore(0)
    job_count = 15 * executor._max_workers
    for _ in range(job_count):
        executor.submit(sem.acquire)
    self.assertEqual(len(executor._processes), executor._max_workers)
    for _ in range(job_count):
        sem.release()
