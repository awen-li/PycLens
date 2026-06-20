# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_argparse.py
# case: TestMessageContentError_test_optional_positional_not_in_message

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    parser = ErrorRaisingArgumentParser(prog='PROG', usage='')
    parser.add_argument('req_pos')
    parser.add_argument('optional_positional', nargs='?', default='eggs')
    with self.assertRaises(ArgumentParserError) as cm:
        parser.parse_args([])
    msg = str(cm.exception)
    self.assertRegex(msg, 'req_pos')
    self.assertNotIn(msg, 'optional_positional')
