# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_argparse.py
# case: TestArgumentTypeError_test_argument_type_error

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def spam(string):
        raise argparse.ArgumentTypeError('spam!')
    parser = ErrorRaisingArgumentParser(prog='PROG', add_help=False)
    parser.add_argument('x', type=spam)
    with self.assertRaises(ArgumentParserError) as cm:
        parser.parse_args(['XXX'])
    self.assertEqual('usage: PROG x\nPROG: error: argument x: spam!\n', cm.exception.stderr)
