# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_sys_settrace.py
# case: RaisingTraceFuncTestCase_test_exception_arguments

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def f():
        x = 0
        x.no_such_attr

    def g(frame, event, arg):
        if event == 'exception':
            (type, exception, trace) = arg
            self.assertIsInstance(exception, Exception)
        return g
    existing = sys.gettrace()
    try:
        sys.settrace(g)
        try:
            f()
        except AttributeError:
            pass
    finally:
        sys.settrace(existing)
