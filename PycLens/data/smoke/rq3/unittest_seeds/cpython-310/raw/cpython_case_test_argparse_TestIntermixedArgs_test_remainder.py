# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_argparse.py
# case: TestIntermixedArgs_test_remainder

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    parser = ErrorRaisingArgumentParser(prog='PROG')
    parser.add_argument('-z')
    parser.add_argument('x')
    parser.add_argument('y', nargs='...')
    argv = 'X A B -z Z'.split()
    with self.assertRaises(TypeError) as cm:
        parser.parse_intermixed_args(argv)
    self.assertRegex(str(cm.exception), '\\.\\.\\.')
