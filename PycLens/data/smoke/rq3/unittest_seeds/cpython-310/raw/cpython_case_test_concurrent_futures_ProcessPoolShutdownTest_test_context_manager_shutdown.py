# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_concurrent_futures.py
# case: ProcessPoolShutdownTest_test_context_manager_shutdown

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with futures.ProcessPoolExecutor(max_workers=5, mp_context=self.get_context()) as e:
        processes = e._processes
        self.assertEqual(list(e.map(abs, range(-5, 5))), [5, 4, 3, 2, 1, 0, 1, 2, 3, 4])
    for p in processes.values():
        p.join()
