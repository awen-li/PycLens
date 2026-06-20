# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_sys_settrace.py
# case: TraceTestCase_test_break_to_continue2

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def func():
        TRUE = 1
        x = [1]
        while x:
            x.pop()
            while TRUE:
                break
            else:
                continue
    self.run_and_compare(func, [(0, 'call'), (1, 'line'), (2, 'line'), (3, 'line'), (4, 'line'), (5, 'line'), (6, 'line'), (3, 'line'), (3, 'return')])
