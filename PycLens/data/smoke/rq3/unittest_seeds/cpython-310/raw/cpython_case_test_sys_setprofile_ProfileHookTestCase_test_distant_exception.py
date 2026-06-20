# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_sys_setprofile.py
# case: ProfileHookTestCase_test_distant_exception

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def f():
        1 / 0

    def g():
        f()

    def h():
        g()

    def i():
        h()

    def j(p):
        i()
    f_ident = ident(f)
    g_ident = ident(g)
    h_ident = ident(h)
    i_ident = ident(i)
    j_ident = ident(j)
    self.check_events(j, [(1, 'call', j_ident), (2, 'call', i_ident), (3, 'call', h_ident), (4, 'call', g_ident), (5, 'call', f_ident), (5, 'return', f_ident), (4, 'return', g_ident), (3, 'return', h_ident), (2, 'return', i_ident), (1, 'return', j_ident)])
