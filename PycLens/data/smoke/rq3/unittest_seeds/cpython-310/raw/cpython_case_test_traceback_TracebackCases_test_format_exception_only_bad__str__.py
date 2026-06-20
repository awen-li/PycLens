# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_traceback.py
# case: TracebackCases_test_format_exception_only_bad__str__

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class X(Exception):

        def __str__(self):
            1 / 0
    err = traceback.format_exception_only(X, X())
    self.assertEqual(len(err), 1)
    str_value = '<unprintable %s object>' % X.__name__
    if X.__module__ in ('__main__', 'builtins'):
        str_name = X.__qualname__
    else:
        str_name = '.'.join([X.__module__, X.__qualname__])
    self.assertEqual(err[0], '%s: %s\n' % (str_name, str_value))
