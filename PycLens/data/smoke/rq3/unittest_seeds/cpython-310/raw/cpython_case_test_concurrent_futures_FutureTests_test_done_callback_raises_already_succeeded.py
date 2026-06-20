# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_concurrent_futures.py
# case: FutureTests_test_done_callback_raises_already_succeeded

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with support.captured_stderr() as stderr:

        def raising_fn(callback_future):
            raise Exception('doh!')
        f = Future()
        f.set_result(5)
        f.add_done_callback(raising_fn)
        self.assertIn('exception calling callback for', stderr.getvalue())
        self.assertIn('doh!', stderr.getvalue())
