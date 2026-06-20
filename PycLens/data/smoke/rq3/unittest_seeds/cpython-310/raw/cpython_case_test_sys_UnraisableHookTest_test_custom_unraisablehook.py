# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_sys.py
# case: UnraisableHookTest_test_custom_unraisablehook

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    hook_args = None

    def hook_func(args):
        nonlocal hook_args
        hook_args = args
    obj = object()
    try:
        with test.support.swap_attr(sys, 'unraisablehook', hook_func):
            expected = self.write_unraisable_exc(ValueError(42), 'custom hook', obj)
            for attr in 'exc_type exc_value exc_traceback err_msg object'.split():
                self.assertEqual(getattr(hook_args, attr), getattr(expected, attr), (hook_args, expected))
    finally:
        expected = None
        hook_args = None
