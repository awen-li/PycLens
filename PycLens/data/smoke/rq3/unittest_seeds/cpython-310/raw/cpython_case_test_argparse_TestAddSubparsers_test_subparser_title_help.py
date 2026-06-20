# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_argparse.py
# case: TestAddSubparsers_test_subparser_title_help

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    parser = ErrorRaisingArgumentParser(prog='PROG', description='main description')
    parser.add_argument('--foo', action='store_true', help='foo help')
    parser.add_argument('bar', help='bar help')
    subparsers = parser.add_subparsers(title='subcommands', description='command help', help='additional text')
    parser1 = subparsers.add_parser('1')
    parser2 = subparsers.add_parser('2')
    self.assertEqual(parser.format_usage(), 'usage: PROG [-h] [--foo] bar {1,2} ...\n')
    self.assertEqual(parser.format_help(), textwrap.dedent('            usage: PROG [-h] [--foo] bar {1,2} ...\n\n            main description\n\n            positional arguments:\n              bar         bar help\n\n            options:\n              -h, --help  show this help message and exit\n              --foo       foo help\n\n            subcommands:\n              command help\n\n              {1,2}       additional text\n            '))
