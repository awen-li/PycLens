# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_configparser.py
# case: ConfigParserTestCaseTrickyFile_test_cfgparser_dot_3

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    tricky = support.findfile('cfgparser.3')
    cf = self.newconfig()
    self.assertEqual(len(cf.read(tricky, encoding='utf-8')), 1)
    self.assertEqual(cf.sections(), ['strange', 'corruption', 'yeah, sections can be indented as well', 'another one!', 'no values here', 'tricky interpolation', 'more interpolation'])
    self.assertEqual(cf.getint(self.default_section, 'go', vars={'interpolate': '-1'}), -1)
    with self.assertRaises(ValueError):
        cf.getint(self.default_section, 'go', raw=True, vars={'interpolate': '-1'})
    self.assertEqual(len(cf.get('strange', 'other').split('\n')), 4)
    self.assertEqual(len(cf.get('corruption', 'value').split('\n')), 10)
    longname = 'yeah, sections can be indented as well'
    self.assertFalse(cf.getboolean(longname, 'are they subsections'))
    self.assertEqual(cf.get(longname, 'lets use some Unicode'), '片仮名')
    self.assertEqual(len(cf.items('another one!')), 5)
    with self.assertRaises(configparser.InterpolationMissingOptionError):
        cf.items('no values here')
    self.assertEqual(cf.get('tricky interpolation', 'lets'), 'do this')
    self.assertEqual(cf.get('tricky interpolation', 'lets'), cf.get('tricky interpolation', 'go'))
    self.assertEqual(cf.get('more interpolation', 'lets'), 'go shopping')
