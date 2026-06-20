# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_argparse.py
# case: TestAddSubparsers_test_required_subparsers_no_destination_error

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    parser = ErrorRaisingArgumentParser()
    subparsers = parser.add_subparsers(required=True)
    subparsers.add_parser('foo')
    subparsers.add_parser('bar')
    with self.assertRaises(ArgumentParserError) as excinfo:
        parser.parse_args(())
    self.assertRegex(excinfo.exception.stderr, 'error: the following arguments are required: {foo,bar}\n$')
