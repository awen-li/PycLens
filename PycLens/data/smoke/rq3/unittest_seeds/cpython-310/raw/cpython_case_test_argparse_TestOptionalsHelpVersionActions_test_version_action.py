# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_argparse.py
# case: TestOptionalsHelpVersionActions_test_version_action

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    parser = ErrorRaisingArgumentParser(prog='XXX')
    parser.add_argument('-V', action='version', version='%(prog)s 3.7')
    with self.assertRaises(ArgumentParserError) as cm:
        parser.parse_args(['-V'])
    self.assertEqual('XXX 3.7\n', cm.exception.stdout)
