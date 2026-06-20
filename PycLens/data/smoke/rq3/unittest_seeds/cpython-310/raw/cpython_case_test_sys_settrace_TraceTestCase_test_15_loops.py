# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_sys_settrace.py
# case: TraceTestCase_test_15_loops

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def for_example():
        for x in range(2):
            pass
    self.run_and_compare(for_example, [(0, 'call'), (1, 'line'), (2, 'line'), (1, 'line'), (2, 'line'), (1, 'line'), (1, 'return')])

    def while_example():
        x = 2
        while x > 0:
            x -= 1
    self.run_and_compare(while_example, [(0, 'call'), (2, 'line'), (3, 'line'), (4, 'line'), (3, 'line'), (4, 'line'), (3, 'line'), (3, 'return')])
