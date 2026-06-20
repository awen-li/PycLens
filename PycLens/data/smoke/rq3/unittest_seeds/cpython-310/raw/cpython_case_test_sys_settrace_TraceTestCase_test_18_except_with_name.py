# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_sys_settrace.py
# case: TraceTestCase_test_18_except_with_name

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def func():
        try:
            try:
                raise Exception
            except Exception as e:
                raise
                x = 'Something'
                y = 'Something'
        except Exception:
            pass
    self.run_and_compare(func, [(0, 'call'), (1, 'line'), (2, 'line'), (3, 'line'), (3, 'exception'), (4, 'line'), (5, 'line'), (8, 'line'), (9, 'line'), (9, 'return')])
