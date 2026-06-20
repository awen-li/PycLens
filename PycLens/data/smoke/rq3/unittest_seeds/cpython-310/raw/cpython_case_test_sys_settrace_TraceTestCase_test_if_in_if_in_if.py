# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_sys_settrace.py
# case: TraceTestCase_test_if_in_if_in_if

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def func(a=0, p=1, z=1):
        if p:
            if a:
                if z:
                    pass
                else:
                    pass
        else:
            pass
    self.run_and_compare(func, [(0, 'call'), (1, 'line'), (2, 'line'), (2, 'return')])
