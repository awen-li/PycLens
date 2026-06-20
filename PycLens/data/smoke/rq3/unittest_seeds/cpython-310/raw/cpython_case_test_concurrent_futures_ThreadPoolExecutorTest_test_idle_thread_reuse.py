# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_concurrent_futures.py
# case: ThreadPoolExecutorTest_test_idle_thread_reuse

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    executor = self.executor_type()
    executor.submit(mul, 21, 2).result()
    executor.submit(mul, 6, 7).result()
    executor.submit(mul, 3, 14).result()
    self.assertEqual(len(executor._threads), 1)
    executor.shutdown(wait=True)
