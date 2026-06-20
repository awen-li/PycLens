# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_sys_settrace.py
# case: TraceTestCase_test_nested_try_if

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def func():
        x = 'hello'
        try:
            3 / 0
        except ZeroDivisionError:
            if x == 'raise':
                raise ValueError()
        f = 7
    self.run_and_compare(func, [(0, 'call'), (1, 'line'), (2, 'line'), (3, 'line'), (3, 'exception'), (4, 'line'), (5, 'line'), (7, 'line'), (7, 'return')])
