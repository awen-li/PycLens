# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_sys_settrace.py
# case: TraceTestCase_test_try_except_no_exception

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def func():
        try:
            2
        except:
            4
        finally:
            6
    self.run_and_compare(func, [(0, 'call'), (1, 'line'), (2, 'line'), (6, 'line'), (6, 'return')])
