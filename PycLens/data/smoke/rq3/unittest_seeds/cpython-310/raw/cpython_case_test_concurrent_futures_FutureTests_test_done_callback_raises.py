# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_concurrent_futures.py
# case: FutureTests_test_done_callback_raises

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with support.captured_stderr() as stderr:
        raising_was_called = False
        fn_was_called = False

        def raising_fn(callback_future):
            nonlocal raising_was_called
            raising_was_called = True
            raise Exception('doh!')

        def fn(callback_future):
            nonlocal fn_was_called
            fn_was_called = True
        f = Future()
        f.add_done_callback(raising_fn)
        f.add_done_callback(fn)
        f.set_result(5)
        self.assertTrue(raising_was_called)
        self.assertTrue(fn_was_called)
        self.assertIn('Exception: doh!', stderr.getvalue())
