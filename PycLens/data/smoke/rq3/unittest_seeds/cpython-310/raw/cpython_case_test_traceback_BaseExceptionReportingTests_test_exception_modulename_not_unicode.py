# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_traceback.py
# case: BaseExceptionReportingTests_test_exception_modulename_not_unicode

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class X(Exception):

        def __str__(self):
            return 'I am X'
    X.__module__ = 42
    err = self.get_report(X())
    exp = f'<unknown>.{X.__qualname__}: I am X\n'
    self.assertEqual(exp, err)
