# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_concurrent_futures.py
# case: ProcessPoolExecutorTest_test_killed_child

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    futures = [self.executor.submit(time.sleep, 3)]
    p = next(iter(self.executor._processes.values()))
    p.terminate()
    for fut in futures:
        self.assertRaises(BrokenProcessPool, fut.result)
    self.assertRaises(BrokenProcessPool, self.executor.submit, pow, 2, 8)
