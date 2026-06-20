# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_configparser.py
# case: ConfigParserTestCase_test_safe_interpolation

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    cf = self.fromstring('[section]\noption1{eq}xxx\noption2{eq}%(option1)s/xxx\nok{eq}%(option1)s/%%s\nnot_ok{eq}%(option2)s/%%s'.format(eq=self.delimiters[0]))
    self.assertEqual(cf.get('section', 'ok'), 'xxx/%s')
    if self.interpolation == configparser._UNSET:
        self.assertEqual(cf.get('section', 'not_ok'), 'xxx/xxx/%s')
    elif isinstance(self.interpolation, configparser.LegacyInterpolation):
        with self.assertRaises(TypeError):
            cf.get('section', 'not_ok')
