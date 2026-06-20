# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_sys_settrace.py
# case: TraceTestCase_test_14_onliner_if

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def onliners():
        if True:
            x = False
        else:
            x = True
        return 0
    self.run_and_compare(onliners, [(0, 'call'), (1, 'line'), (3, 'line'), (3, 'return')])
