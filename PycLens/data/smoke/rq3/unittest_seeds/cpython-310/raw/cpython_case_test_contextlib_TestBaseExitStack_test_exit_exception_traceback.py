# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_contextlib.py
# case: TestBaseExitStack_test_exit_exception_traceback

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def raise_exc(exc):
        raise exc
    try:
        with self.exit_stack() as stack:
            stack.callback(raise_exc, ValueError)
            1 / 0
    except ValueError as e:
        exc = e
    self.assertIsInstance(exc, ValueError)
    ve_frames = traceback.extract_tb(exc.__traceback__)
    expected = [('test_exit_exception_traceback', 'with self.exit_stack() as stack:')] + self.callback_error_internal_frames + [('_exit_wrapper', 'callback(*args, **kwds)'), ('raise_exc', 'raise exc')]
    self.assertEqual([(f.name, f.line) for f in ve_frames], expected)
    self.assertIsInstance(exc.__context__, ZeroDivisionError)
    zde_frames = traceback.extract_tb(exc.__context__.__traceback__)
    self.assertEqual([(f.name, f.line) for f in zde_frames], [('test_exit_exception_traceback', '1/0')])
