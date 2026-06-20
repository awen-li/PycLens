# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_sys_settrace.py
# case: TraceTestCase_test_if_break

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def func():
        seq = [1, 0]
        while seq:
            n = seq.pop()
            if n:
                break
        else:
            n = 99
        return n
    self.run_and_compare(func, [(0, 'call'), (1, 'line'), (2, 'line'), (3, 'line'), (4, 'line'), (2, 'line'), (3, 'line'), (4, 'line'), (5, 'line'), (8, 'line'), (8, 'return')])
