# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_configparser.py
# case: ConfigParserTestCase_test_interpolation_missing_value

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    cf = self.get_interpolation_config()
    e = self.get_error(cf, configparser.InterpolationMissingOptionError, 'Interpolation Error', 'name')
    self.assertEqual(e.reference, 'reference')
    self.assertEqual(e.section, 'Interpolation Error')
    self.assertEqual(e.option, 'name')
    if self.interpolation == configparser._UNSET:
        self.assertEqual(e.args, ('name', 'Interpolation Error', '%(reference)s', 'reference'))
    elif isinstance(self.interpolation, configparser.LegacyInterpolation):
        self.assertEqual(e.args, ('name', 'Interpolation Error', '%(reference)s', 'reference'))
