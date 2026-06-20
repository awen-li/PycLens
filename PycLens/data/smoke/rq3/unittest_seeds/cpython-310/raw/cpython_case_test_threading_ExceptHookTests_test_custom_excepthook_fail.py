# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_threading.py
# case: ExceptHookTests_test_custom_excepthook_fail

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def threading_hook(args):
        raise ValueError('threading_hook failed')
    err_str = None

    def sys_hook(exc_type, exc_value, exc_traceback):
        nonlocal err_str
        err_str = str(exc_value)
    with support.swap_attr(threading, 'excepthook', threading_hook), support.swap_attr(sys, 'excepthook', sys_hook), support.captured_output('stderr') as stderr:
        thread = ThreadRunFail()
        thread.start()
        thread.join()
    self.assertEqual(stderr.getvalue(), 'Exception in threading.excepthook:\n')
    self.assertEqual(err_str, 'threading_hook failed')
