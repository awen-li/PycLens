# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_concurrent_futures.py
# case: ExecutorDeadlockTest_test_shutdown_deadlock_pickle

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.executor.shutdown(wait=True)
    with self.executor_type(max_workers=2, mp_context=self.get_context()) as executor:
        self.executor = executor
        executor.submit(id, 42).result()
        executor_manager = executor._executor_manager_thread
        f = executor.submit(id, ErrorAtPickle())
        executor.shutdown(wait=False)
        with self.assertRaises(PicklingError):
            f.result()
    executor_manager.join()
