# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_sys.py
# case: UnraisableHookTest_test_custom_unraisablehook_fail

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def hook_func(*args):
        raise Exception('hook_func failed')
    with test.support.captured_output('stderr') as stderr:
        with test.support.swap_attr(sys, 'unraisablehook', hook_func):
            self.write_unraisable_exc(ValueError(42), 'custom hook fail', None)
    err = stderr.getvalue()
    self.assertIn(f'Exception ignored in sys.unraisablehook: {hook_func!r}\n', err)
    self.assertIn('Traceback (most recent call last):\n', err)
    self.assertIn('Exception: hook_func failed\n', err)
