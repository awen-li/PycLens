# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_functools.py
# case: TestSingleDispatch_test_register_decorator

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    @functools.singledispatch
    def g(obj):
        return 'base'

    @g.register(int)
    def g_int(i):
        return 'int %s' % (i,)
    self.assertEqual(g(''), 'base')
    self.assertEqual(g(12), 'int 12')
    self.assertIs(g.dispatch(int), g_int)
    self.assertIs(g.dispatch(object), g.dispatch(str))
