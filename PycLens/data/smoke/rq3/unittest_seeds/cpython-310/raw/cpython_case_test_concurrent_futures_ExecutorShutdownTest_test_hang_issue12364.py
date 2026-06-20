# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_concurrent_futures.py
# case: ExecutorShutdownTest_test_hang_issue12364

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    fs = [self.executor.submit(time.sleep, 0.1) for _ in range(50)]
    self.executor.shutdown()
    for f in fs:
        f.result()
