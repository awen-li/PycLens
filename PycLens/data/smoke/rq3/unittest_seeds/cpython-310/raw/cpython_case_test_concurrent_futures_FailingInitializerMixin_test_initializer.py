# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_concurrent_futures.py
# case: FailingInitializerMixin_test_initializer

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with self._assert_logged('ValueError: error in initializer'):
        try:
            future = self.executor.submit(get_init_status)
        except BrokenExecutor:
            pass
        else:
            with self.assertRaises(BrokenExecutor):
                future.result()
        t1 = time.monotonic()
        while not self.executor._broken:
            if time.monotonic() - t1 > 5:
                self.fail('executor not broken after 5 s.')
            time.sleep(0.01)
        with self.assertRaises(BrokenExecutor):
            self.executor.submit(get_init_status)
