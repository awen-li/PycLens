# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_argparse.py
# case: TestAddSubparsers_test_help_alternate_prefix_chars

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    parser = self._get_parser(prefix_chars='+:/')
    self.assertEqual(parser.format_usage(), 'usage: PROG [+h] [++foo] bar {1,2,3} ...\n')
    self.assertEqual(parser.format_help(), textwrap.dedent('            usage: PROG [+h] [++foo] bar {1,2,3} ...\n\n            main description\n\n            positional arguments:\n              bar         bar help\n              {1,2,3}     command help\n\n            options:\n              +h, ++help  show this help message and exit\n              ++foo       foo help\n            '))
