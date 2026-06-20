# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_concurrent_futures.py
# case: ProcessPoolExecutorTest_test_traceback

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    future = self.executor.submit(self._test_traceback)
    with self.assertRaises(Exception) as cm:
        future.result()
    exc = cm.exception
    self.assertIs(type(exc), RuntimeError)
    self.assertEqual(exc.args, (123,))
    cause = exc.__cause__
    self.assertIs(type(cause), futures.process._RemoteTraceback)
    self.assertIn('raise RuntimeError(123) # some comment', cause.tb)
    with support.captured_stderr() as f1:
        try:
            raise exc
        except RuntimeError:
            sys.excepthook(*sys.exc_info())
    self.assertIn('raise RuntimeError(123) # some comment', f1.getvalue())
