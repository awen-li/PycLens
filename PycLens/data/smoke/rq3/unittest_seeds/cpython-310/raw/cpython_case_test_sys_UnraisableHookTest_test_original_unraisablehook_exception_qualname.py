# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_sys.py
# case: UnraisableHookTest_test_original_unraisablehook_exception_qualname

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class A:

        class B:

            class X(Exception):
                pass
    with test.support.captured_stderr() as stderr, test.support.swap_attr(sys, 'unraisablehook', sys.__unraisablehook__):
        expected = self.write_unraisable_exc(A.B.X(), 'msg', 'obj')
    report = stderr.getvalue()
    testName = 'test_original_unraisablehook_exception_qualname'
    self.assertIn(f'{testName}.<locals>.A.B.X', report)
