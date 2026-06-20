# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_threading.py
# case: ExceptHookTests_test_excepthook_thread_None

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with support.captured_output('stderr') as stderr:
        try:
            raise ValueError('bug')
        except Exception as exc:
            args = threading.ExceptHookArgs([*sys.exc_info(), None])
            try:
                threading.excepthook(args)
            finally:
                args = None
    stderr = stderr.getvalue().strip()
    self.assertIn(f'Exception in thread {threading.get_ident()}:\n', stderr)
    self.assertIn('Traceback (most recent call last):\n', stderr)
    self.assertIn('  raise ValueError("bug")', stderr)
    self.assertIn('ValueError: bug', stderr)
