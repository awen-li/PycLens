# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_functools.py
# case: TestSingleDispatch_test_c_classes

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    @functools.singledispatch
    def g(obj):
        return 'base'

    @g.register(decimal.DecimalException)
    def _(obj):
        return obj.args
    subn = decimal.Subnormal('Exponent < Emin')
    rnd = decimal.Rounded('Number got rounded')
    self.assertEqual(g(subn), ('Exponent < Emin',))
    self.assertEqual(g(rnd), ('Number got rounded',))

    @g.register(decimal.Subnormal)
    def _(obj):
        return 'Too small to care.'
    self.assertEqual(g(subn), 'Too small to care.')
    self.assertEqual(g(rnd), ('Number got rounded',))
