# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_argparse.py
# case: TestOptionalsHelpVersionActions_test_version_format

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    parser = ErrorRaisingArgumentParser(prog='PPP')
    parser.add_argument('-v', '--version', action='version', version='%(prog)s 3.5')
    with self.assertRaises(ArgumentParserError) as cm:
        parser.parse_args(['-v'])
    self.assertEqual('PPP 3.5\n', cm.exception.stdout)
