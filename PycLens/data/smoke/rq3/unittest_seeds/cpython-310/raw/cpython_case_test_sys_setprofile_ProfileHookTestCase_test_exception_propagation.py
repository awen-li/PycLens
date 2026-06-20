# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_sys_setprofile.py
# case: ProfileHookTestCase_test_exception_propagation

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def f(p):
        1 / 0

    def g(p):
        try:
            f(p)
        finally:
            p.add_event('falling through')
    f_ident = ident(f)
    g_ident = ident(g)
    self.check_events(g, [(1, 'call', g_ident), (2, 'call', f_ident), (2, 'return', f_ident), (1, 'falling through', g_ident), (1, 'return', g_ident)])
