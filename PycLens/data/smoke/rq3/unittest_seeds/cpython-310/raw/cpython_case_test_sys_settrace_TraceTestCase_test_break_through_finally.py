# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_sys_settrace.py
# case: TraceTestCase_test_break_through_finally

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def func():
        (a, c, d, i) = (1, 1, 1, 99)
        try:
            for i in range(3):
                try:
                    a = 5
                    if i > 0:
                        break
                    a = 8
                finally:
                    c = 10
        except:
            d = 12
        assert a == 5 and c == 10 and (d == 1)
    self.run_and_compare(func, [(0, 'call'), (1, 'line'), (2, 'line'), (3, 'line'), (4, 'line'), (5, 'line'), (6, 'line'), (8, 'line'), (10, 'line'), (3, 'line'), (4, 'line'), (5, 'line'), (6, 'line'), (7, 'line'), (10, 'line'), (13, 'line'), (13, 'return')])
