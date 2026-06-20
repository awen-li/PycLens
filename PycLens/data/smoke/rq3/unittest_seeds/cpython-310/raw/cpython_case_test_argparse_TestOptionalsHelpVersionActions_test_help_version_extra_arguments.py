# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_argparse.py
# case: TestOptionalsHelpVersionActions_test_help_version_extra_arguments

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    parser = ErrorRaisingArgumentParser()
    parser.add_argument('--version', action='version', version='1.0')
    parser.add_argument('-x', action='store_true')
    parser.add_argument('y')
    valid_prefixes = ['', '-x', 'foo', '-x bar', 'baz -x']
    valid_suffixes = valid_prefixes + ['--bad-option', 'foo bar baz']
    for prefix in valid_prefixes:
        for suffix in valid_suffixes:
            format = '%s %%s %s' % (prefix, suffix)
        self.assertPrintHelpExit(parser, format % '-h')
        self.assertPrintHelpExit(parser, format % '--help')
        self.assertRaises(AttributeError, getattr, parser, 'format_version')
