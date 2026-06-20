# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_argparse.py
# case: TestAddSubparsers_test_help_blank

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    parser = ErrorRaisingArgumentParser(prog='PROG', description='main description')
    parser.add_argument('foo', help='    ')
    self.assertEqual(parser.format_help(), textwrap.dedent('            usage: PROG [-h] foo\n\n            main description\n\n            positional arguments:\n              foo         \n\n            options:\n              -h, --help  show this help message and exit\n        '))
    parser = ErrorRaisingArgumentParser(prog='PROG', description='main description')
    parser.add_argument('foo', choices=[], help='%(choices)s')
    self.assertEqual(parser.format_help(), textwrap.dedent('            usage: PROG [-h] {}\n\n            main description\n\n            positional arguments:\n              {}          \n\n            options:\n              -h, --help  show this help message and exit\n        '))
