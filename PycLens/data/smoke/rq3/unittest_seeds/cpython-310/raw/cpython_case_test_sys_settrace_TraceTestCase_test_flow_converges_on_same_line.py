# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_sys_settrace.py
# case: TraceTestCase_test_flow_converges_on_same_line

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def foo(x):
        if x:
            try:
                1 / (x - 1)
            except ZeroDivisionError:
                pass
        return x

    def func():
        for i in range(2):
            foo(i)
    self.run_and_compare(func, [(0, 'call'), (1, 'line'), (2, 'line'), (-8, 'call'), (-7, 'line'), (-2, 'line'), (-2, 'return'), (1, 'line'), (2, 'line'), (-8, 'call'), (-7, 'line'), (-6, 'line'), (-5, 'line'), (-5, 'exception'), (-4, 'line'), (-3, 'line'), (-2, 'line'), (-2, 'return'), (1, 'line'), (1, 'return')])
