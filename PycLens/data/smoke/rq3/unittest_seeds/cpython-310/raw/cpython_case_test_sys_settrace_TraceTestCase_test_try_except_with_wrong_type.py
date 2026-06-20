# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_sys_settrace.py
# case: TraceTestCase_test_try_except_with_wrong_type

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def func():
        try:
            2 / 0
        except IndexError:
            4
        finally:
            return 6
    self.run_and_compare(func, [(0, 'call'), (1, 'line'), (2, 'line'), (2, 'exception'), (3, 'line'), (6, 'line'), (6, 'return')])
