# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_concurrent_futures.py
# case: ThreadPoolShutdownTest_test_del_shutdown

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    executor = futures.ThreadPoolExecutor(max_workers=5)
    res = executor.map(abs, range(-5, 5))
    threads = executor._threads
    del executor
    for t in threads:
        t.join()
    assert all([r == abs(v) for (r, v) in zip(res, range(-5, 5))])
