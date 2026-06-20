# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_concurrent_futures.py
# case: ThreadPoolShutdownTest_test_context_manager_shutdown

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with futures.ThreadPoolExecutor(max_workers=5) as e:
        executor = e
        self.assertEqual(list(e.map(abs, range(-5, 5))), [5, 4, 3, 2, 1, 0, 1, 2, 3, 4])
    for t in executor._threads:
        t.join()
