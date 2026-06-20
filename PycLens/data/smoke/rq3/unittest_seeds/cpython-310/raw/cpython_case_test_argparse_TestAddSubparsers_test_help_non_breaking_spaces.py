# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_argparse.py
# case: TestAddSubparsers_test_help_non_breaking_spaces

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    parser = ErrorRaisingArgumentParser(prog='PROG', description='main description')
    parser.add_argument('--non-breaking', action='store_false', help='help message containing non-breaking spaces shall not wrap\xa0at non-breaking spaces')
    self.assertEqual(parser.format_help(), textwrap.dedent('            usage: PROG [-h] [--non-breaking]\n\n            main description\n\n            options:\n              -h, --help      show this help message and exit\n              --non-breaking  help message containing non-breaking spaces shall not\n                              wrap\xa0at non-breaking spaces\n        '))
