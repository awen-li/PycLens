# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_functools.py
# case: TestSingleDispatch_test_simple_overloads

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    @functools.singledispatch
    def g(obj):
        return 'base'

    def g_int(i):
        return 'integer'
    g.register(int, g_int)
    self.assertEqual(g('str'), 'base')
    self.assertEqual(g(1), 'integer')
    self.assertEqual(g([1, 2, 3]), 'base')
