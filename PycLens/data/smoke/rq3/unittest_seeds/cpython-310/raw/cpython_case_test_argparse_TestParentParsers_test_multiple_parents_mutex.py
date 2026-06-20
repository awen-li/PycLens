# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_argparse.py
# case: TestParentParsers_test_multiple_parents_mutex

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    parents = [self.ab_mutex_parent, self.wxyz_parent]
    parser = ErrorRaisingArgumentParser(parents=parents)
    self.assertEqual(parser.parse_args('-a --w 2 3'.split()), NS(a=True, b=False, w='2', y=None, z='3'))
    self.assertArgumentParserError(parser.parse_args, '-a --w 2 3 -b'.split())
    self.assertArgumentParserError(parser.parse_args, '-a -b --w 2 3'.split())
