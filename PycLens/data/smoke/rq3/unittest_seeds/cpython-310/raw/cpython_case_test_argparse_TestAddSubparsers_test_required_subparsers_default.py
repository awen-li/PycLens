# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_argparse.py
# case: TestAddSubparsers_test_required_subparsers_default

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    parser = ErrorRaisingArgumentParser()
    subparsers = parser.add_subparsers(dest='command')
    subparsers.add_parser('run')
    ret = parser.parse_args(())
    self.assertIsNone(ret.command)
