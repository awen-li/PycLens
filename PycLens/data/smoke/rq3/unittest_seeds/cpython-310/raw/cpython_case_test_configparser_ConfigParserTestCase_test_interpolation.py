# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_configparser.py
# case: ConfigParserTestCase_test_interpolation

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    cf = self.get_interpolation_config()
    eq = self.assertEqual
    eq(cf.get('Foo', 'bar'), 'something with interpolation (1 step)')
    eq(cf.get('Foo', 'bar9'), 'something with lots of interpolation (9 steps)')
    eq(cf.get('Foo', 'bar10'), 'something with lots of interpolation (10 steps)')
    e = self.get_error(cf, configparser.InterpolationDepthError, 'Foo', 'bar11')
    if self.interpolation == configparser._UNSET:
        self.assertEqual(e.args, ('bar11', 'Foo', 'something %(with11)s lots of interpolation (11 steps)'))
    elif isinstance(self.interpolation, configparser.LegacyInterpolation):
        self.assertEqual(e.args, ('bar11', 'Foo', 'something %(with11)s lots of interpolation (11 steps)'))
