# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_sys_setprofile.py
# case: ProfileHookTestCase_test_generator

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def f():
        for i in range(2):
            yield i

    def g(p):
        for i in f():
            pass
    f_ident = ident(f)
    g_ident = ident(g)
    self.check_events(g, [(1, 'call', g_ident), (2, 'call', f_ident), (2, 'return', f_ident), (2, 'call', f_ident), (2, 'return', f_ident), (2, 'call', f_ident), (2, 'return', f_ident), (1, 'return', g_ident)])
