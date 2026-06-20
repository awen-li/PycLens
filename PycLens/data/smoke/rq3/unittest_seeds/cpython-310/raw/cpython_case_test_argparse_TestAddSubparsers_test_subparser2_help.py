# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_argparse.py
# case: TestAddSubparsers_test_subparser2_help

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self._test_subparser_help('5.0 2 -h', textwrap.dedent('            usage: PROG bar 2 [-h] [-y {1,2,3}] [z ...]\n\n            2 description\n\n            positional arguments:\n              z           z help\n\n            options:\n              -h, --help  show this help message and exit\n              -y {1,2,3}  y help\n            '))
