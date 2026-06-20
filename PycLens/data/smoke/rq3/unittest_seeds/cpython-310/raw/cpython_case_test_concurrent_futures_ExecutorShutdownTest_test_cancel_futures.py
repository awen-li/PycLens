# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_concurrent_futures.py
# case: ExecutorShutdownTest_test_cancel_futures

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    assert self.worker_count <= 5, 'test needs few workers'
    fs = [self.executor.submit(time.sleep, 0.1) for _ in range(50)]
    self.executor.shutdown(cancel_futures=True)
    cancelled = [fut for fut in fs if fut.cancelled()]
    self.assertGreater(len(cancelled), 20)
    others = [fut for fut in fs if not fut.cancelled()]
    for fut in others:
        self.assertTrue(fut.done(), msg=f'fut._state={fut._state!r}')
        self.assertIsNone(fut.exception())
    self.assertGreater(len(others), 0)
