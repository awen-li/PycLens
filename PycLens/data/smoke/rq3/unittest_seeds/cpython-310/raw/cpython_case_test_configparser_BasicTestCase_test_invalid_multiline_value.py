# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_configparser.py
# case: BasicTestCase_test_invalid_multiline_value

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    if self.allow_no_value:
        self.skipTest('if no_value is allowed, ParsingError is not raised')
    invalid = textwrap.dedent('            [DEFAULT]\n            test {0} test\n            invalid'.format(self.delimiters[0]))
    cf = self.newconfig()
    with self.assertRaises(configparser.ParsingError):
        cf.read_string(invalid)
    self.assertEqual(cf.get('DEFAULT', 'test'), 'test')
    self.assertEqual(cf['DEFAULT']['test'], 'test')
