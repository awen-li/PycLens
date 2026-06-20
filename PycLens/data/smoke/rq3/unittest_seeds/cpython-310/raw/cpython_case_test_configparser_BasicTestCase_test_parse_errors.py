# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_configparser.py
# case: BasicTestCase_test_parse_errors

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    cf = self.newconfig()
    self.parse_error(cf, configparser.ParsingError, '[Foo]\n{}val-without-opt-name\n'.format(self.delimiters[0]))
    self.parse_error(cf, configparser.ParsingError, '[Foo]\n{}val-without-opt-name\n'.format(self.delimiters[1]))
    e = self.parse_error(cf, configparser.MissingSectionHeaderError, 'No Section!\n')
    self.assertEqual(e.args, ('<???>', 1, 'No Section!\n'))
    if not self.allow_no_value:
        e = self.parse_error(cf, configparser.ParsingError, '[Foo]\n  wrong-indent\n')
        self.assertEqual(e.args, ('<???>',))
        tricky = support.findfile('cfgparser.3')
        if self.delimiters[0] == '=':
            error = configparser.ParsingError
            expected = (tricky,)
        else:
            error = configparser.MissingSectionHeaderError
            expected = (tricky, 1, '  # INI with as many tricky parts as possible\n')
        with open(tricky, encoding='utf-8') as f:
            e = self.parse_error(cf, error, f)
        self.assertEqual(e.args, expected)
