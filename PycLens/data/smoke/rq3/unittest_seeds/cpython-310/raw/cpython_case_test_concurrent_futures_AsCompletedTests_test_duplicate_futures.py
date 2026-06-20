# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_concurrent_futures.py
# case: AsCompletedTests_test_duplicate_futures

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    future1 = self.executor.submit(time.sleep, 2)
    completed = [f for f in futures.as_completed(itertools.repeat(future1, 3))]
    self.assertEqual(len(completed), 1)
