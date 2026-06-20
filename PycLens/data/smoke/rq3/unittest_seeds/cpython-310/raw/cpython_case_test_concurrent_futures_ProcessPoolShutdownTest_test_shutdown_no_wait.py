# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_concurrent_futures.py
# case: ProcessPoolShutdownTest_test_shutdown_no_wait

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    executor = futures.ProcessPoolExecutor(max_workers=5, mp_context=self.get_context())
    res = executor.map(abs, range(-5, 5))
    processes = executor._processes
    call_queue = executor._call_queue
    executor_manager_thread = executor._executor_manager_thread
    executor.shutdown(wait=False)
    executor_manager_thread.join()
    for p in processes.values():
        p.join()
    call_queue.join_thread()
    assert all([r == abs(v) for (r, v) in zip(res, range(-5, 5))])
