# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_concurrent_futures.py
# case: ProcessPoolExecutorTest_test_idle_process_reuse_one

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    executor = self.executor
    assert executor._max_workers >= 4
    if self.get_context().get_start_method(allow_none=False) == 'fork':
        raise unittest.SkipTest('Incompatible with the fork start method.')
    executor.submit(mul, 21, 2).result()
    executor.submit(mul, 6, 7).result()
    executor.submit(mul, 3, 14).result()
    self.assertEqual(len(executor._processes), 1)
