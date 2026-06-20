# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_argparse.py
# case: TestMutuallyExclusiveGroupErrors_test_help

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    parser = ErrorRaisingArgumentParser(prog='PROG')
    group1 = parser.add_mutually_exclusive_group()
    group1.add_argument('--foo', action='store_true')
    group1.add_argument('--bar', action='store_false')
    group2 = parser.add_mutually_exclusive_group()
    group2.add_argument('--soup', action='store_true')
    group2.add_argument('--nuts', action='store_false')
    expected = '            usage: PROG [-h] [--foo | --bar] [--soup | --nuts]\n\n            options:\n              -h, --help  show this help message and exit\n              --foo\n              --bar\n              --soup\n              --nuts\n              '
    self.assertEqual(parser.format_help(), textwrap.dedent(expected))
