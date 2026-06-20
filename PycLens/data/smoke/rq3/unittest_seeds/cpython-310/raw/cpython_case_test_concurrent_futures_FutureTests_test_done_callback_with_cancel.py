# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_concurrent_futures.py
# case: FutureTests_test_done_callback_with_cancel

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    was_cancelled = None

    def fn(callback_future):
        nonlocal was_cancelled
        was_cancelled = callback_future.cancelled()
    f = Future()
    f.add_done_callback(fn)
    self.assertTrue(f.cancel())
    self.assertTrue(was_cancelled)
