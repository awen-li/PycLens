# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_argparse.py
# case: TestIntermixedMessageContentError_test_missing_argument_name_in_message

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    parser = ErrorRaisingArgumentParser(prog='PROG', usage='')
    parser.add_argument('req_pos', type=str)
    parser.add_argument('-req_opt', type=int, required=True)
    with self.assertRaises(ArgumentParserError) as cm:
        parser.parse_args([])
    msg = str(cm.exception)
    self.assertRegex(msg, 'req_pos')
    self.assertRegex(msg, 'req_opt')
    with self.assertRaises(ArgumentParserError) as cm:
        parser.parse_intermixed_args([])
    msg = str(cm.exception)
    self.assertNotRegex(msg, 'req_pos')
    self.assertRegex(msg, 'req_opt')
