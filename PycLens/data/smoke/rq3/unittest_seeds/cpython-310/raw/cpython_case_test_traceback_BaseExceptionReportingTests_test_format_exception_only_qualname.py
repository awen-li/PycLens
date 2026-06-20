# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_traceback.py
# case: BaseExceptionReportingTests_test_format_exception_only_qualname

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class A:

        class B:

            class X(Exception):

                def __str__(self):
                    return 'I am X'
                pass
    err = self.get_report(A.B.X())
    str_value = 'I am X'
    str_name = '.'.join([A.B.X.__module__, A.B.X.__qualname__])
    exp = '%s: %s\n' % (str_name, str_value)
    self.assertEqual(exp, err)
