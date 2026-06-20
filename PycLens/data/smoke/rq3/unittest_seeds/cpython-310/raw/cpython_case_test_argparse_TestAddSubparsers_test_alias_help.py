# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_argparse.py
# case: TestAddSubparsers_test_alias_help

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    parser = self._get_parser(aliases=True, subparser_help=True)
    self.maxDiff = None
    self.assertEqual(parser.format_help(), textwrap.dedent('            usage: PROG [-h] [--foo] bar COMMAND ...\n\n            main description\n\n            positional arguments:\n              bar                   bar help\n\n            options:\n              -h, --help            show this help message and exit\n              --foo                 foo help\n\n            commands:\n              COMMAND\n                1 (1alias1, 1alias2)\n                                    1 help\n                2                   2 help\n                3                   3 help\n            '))
