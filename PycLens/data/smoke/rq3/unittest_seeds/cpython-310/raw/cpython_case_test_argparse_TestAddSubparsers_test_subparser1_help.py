# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_argparse.py
# case: TestAddSubparsers_test_subparser1_help

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self._test_subparser_help('5.0 1 -h', textwrap.dedent('            usage: PROG bar 1 [-h] [-w W] {a,b,c}\n\n            1 description\n\n            positional arguments:\n              {a,b,c}     x help\n\n            options:\n              -h, --help  show this help message and exit\n              -w W        w help\n            '))
