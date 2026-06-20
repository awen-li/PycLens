# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_concurrent_futures.py
# case: FutureTests_test_done_callback_with_result

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    callback_result = None

    def fn(callback_future):
        nonlocal callback_result
        callback_result = callback_future.result()
    f = Future()
    f.add_done_callback(fn)
    f.set_result(5)
    self.assertEqual(5, callback_result)
