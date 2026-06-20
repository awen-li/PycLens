# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_argparse.py
# case: TestMutuallyExclusiveGroupErrors_test_invalid_add_argument

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    parser = ErrorRaisingArgumentParser()
    group = parser.add_mutually_exclusive_group()
    add_argument = group.add_argument
    raises = self.assertRaises
    raises(ValueError, add_argument, '--foo', required=True)
    raises(ValueError, add_argument, 'bar')
    raises(ValueError, add_argument, 'bar', nargs='+')
    raises(ValueError, add_argument, 'bar', nargs=1)
    raises(ValueError, add_argument, 'bar', nargs=argparse.PARSER)
