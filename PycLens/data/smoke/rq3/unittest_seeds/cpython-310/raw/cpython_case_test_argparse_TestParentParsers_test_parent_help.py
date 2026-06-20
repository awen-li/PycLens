# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_argparse.py
# case: TestParentParsers_test_parent_help

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    parents = [self.abcd_parent, self.wxyz_parent]
    parser = ErrorRaisingArgumentParser(parents=parents)
    parser_help = parser.format_help()
    progname = self.main_program
    self.assertEqual(parser_help, textwrap.dedent('            usage: {}{}[-h] [-b B] [--d D] [--w W] [-y Y] a z\n\n            positional arguments:\n              a\n              z\n\n            options:\n              -h, --help  show this help message and exit\n              -b B\n              --w W\n\n            c:\n              --d D\n\n            x:\n              -y Y\n        '.format(progname, ' ' if progname else '')))
