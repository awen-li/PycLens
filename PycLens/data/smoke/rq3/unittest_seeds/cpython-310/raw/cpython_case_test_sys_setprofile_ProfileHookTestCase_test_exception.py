# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_sys_setprofile.py
# case: ProfileHookTestCase_test_exception

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def f(p):
        1 / 0
    f_ident = ident(f)
    self.check_events(f, [(1, 'call', f_ident), (1, 'return', f_ident)])
