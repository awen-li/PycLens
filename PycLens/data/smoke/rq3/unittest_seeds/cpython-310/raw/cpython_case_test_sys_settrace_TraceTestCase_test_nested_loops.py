# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_sys_settrace.py
# case: TraceTestCase_test_nested_loops

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def func():
        for i in range(2):
            for j in range(2):
                a = i + j
        return a == 1
    self.run_and_compare(func, [(0, 'call'), (1, 'line'), (2, 'line'), (3, 'line'), (2, 'line'), (3, 'line'), (2, 'line'), (1, 'line'), (2, 'line'), (3, 'line'), (2, 'line'), (3, 'line'), (2, 'line'), (1, 'line'), (4, 'line'), (4, 'return')])
