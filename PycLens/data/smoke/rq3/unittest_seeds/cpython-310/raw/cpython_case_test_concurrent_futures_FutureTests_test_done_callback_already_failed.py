# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_concurrent_futures.py
# case: FutureTests_test_done_callback_already_failed

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    callback_exception = None

    def fn(callback_future):
        nonlocal callback_exception
        callback_exception = callback_future.exception()
    f = Future()
    f.set_exception(Exception('test'))
    f.add_done_callback(fn)
    self.assertEqual(('test',), callback_exception.args)
