# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_sys.py
# case: UnraisableHookTest_test_original_unraisablehook_wrong_type

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    exc = ValueError(42)
    with test.support.swap_attr(sys, 'unraisablehook', sys.__unraisablehook__):
        with self.assertRaises(TypeError):
            sys.unraisablehook(exc)
