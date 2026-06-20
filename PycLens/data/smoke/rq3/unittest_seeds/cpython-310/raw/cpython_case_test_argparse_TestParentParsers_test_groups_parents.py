# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_argparse.py
# case: TestParentParsers_test_groups_parents

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    parent = ErrorRaisingArgumentParser(add_help=False)
    g = parent.add_argument_group(title='g', description='gd')
    g.add_argument('-w')
    g.add_argument('-x')
    m = parent.add_mutually_exclusive_group()
    m.add_argument('-y')
    m.add_argument('-z')
    parser = ErrorRaisingArgumentParser(parents=[parent])
    self.assertRaises(ArgumentParserError, parser.parse_args, ['-y', 'Y', '-z', 'Z'])
    parser_help = parser.format_help()
    progname = self.main_program
    self.assertEqual(parser_help, textwrap.dedent('            usage: {}{}[-h] [-w W] [-x X] [-y Y | -z Z]\n\n            options:\n              -h, --help  show this help message and exit\n              -y Y\n              -z Z\n\n            g:\n              gd\n\n              -w W\n              -x X\n        '.format(progname, ' ' if progname else '')))
