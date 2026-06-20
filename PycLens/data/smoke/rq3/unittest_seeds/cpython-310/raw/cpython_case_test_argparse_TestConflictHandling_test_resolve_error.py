# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_argparse.py
# case: TestConflictHandling_test_resolve_error

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    get_parser = argparse.ArgumentParser
    parser = get_parser(prog='PROG', conflict_handler='resolve')
    parser.add_argument('-x', help='OLD X')
    parser.add_argument('-x', help='NEW X')
    self.assertEqual(parser.format_help(), textwrap.dedent('            usage: PROG [-h] [-x X]\n\n            options:\n              -h, --help  show this help message and exit\n              -x X        NEW X\n            '))
    parser.add_argument('--spam', metavar='OLD_SPAM')
    parser.add_argument('--spam', metavar='NEW_SPAM')
    self.assertEqual(parser.format_help(), textwrap.dedent('            usage: PROG [-h] [-x X] [--spam NEW_SPAM]\n\n            options:\n              -h, --help       show this help message and exit\n              -x X             NEW X\n              --spam NEW_SPAM\n            '))
