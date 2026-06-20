# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_sys.py
# case: UnraisableHookTest_test_original_unraisablehook_err

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class BrokenDel:

        def __del__(self):
            exc = ValueError('del is broken')
            raise exc

    class BrokenStrException(Exception):

        def __str__(self):
            raise Exception('str() is broken')

    class BrokenExceptionDel:

        def __del__(self):
            exc = BrokenStrException()
            raise exc
    for test_class in (BrokenDel, BrokenExceptionDel):
        with self.subTest(test_class):
            obj = test_class()
            with test.support.captured_stderr() as stderr, test.support.swap_attr(sys, 'unraisablehook', sys.__unraisablehook__):
                del obj
            report = stderr.getvalue()
            self.assertIn('Exception ignored', report)
            self.assertIn(test_class.__del__.__qualname__, report)
            self.assertIn('test_sys.py', report)
            self.assertIn('raise exc', report)
            if test_class is BrokenExceptionDel:
                self.assertIn('BrokenStrException', report)
                self.assertIn('<exception str() failed>', report)
            else:
                self.assertIn('ValueError', report)
                self.assertIn('del is broken', report)
            self.assertTrue(report.endswith('\n'))
