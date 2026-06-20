# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_argparse.py
# case: TestAddSubparsers_test_parse_known_args

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertEqual(self.parser.parse_known_args('0.5 1 b -w 7'.split()), (NS(foo=False, bar=0.5, w=7, x='b'), []))
    self.assertEqual(self.parser.parse_known_args('0.5 -p 1 b -w 7'.split()), (NS(foo=False, bar=0.5, w=7, x='b'), ['-p']))
    self.assertEqual(self.parser.parse_known_args('0.5 1 b -w 7 -p'.split()), (NS(foo=False, bar=0.5, w=7, x='b'), ['-p']))
    self.assertEqual(self.parser.parse_known_args('0.5 1 b -q -rs -w 7'.split()), (NS(foo=False, bar=0.5, w=7, x='b'), ['-q', '-rs']))
    self.assertEqual(self.parser.parse_known_args('0.5 -W 1 b -X Y -w 7 Z'.split()), (NS(foo=False, bar=0.5, w=7, x='b'), ['-W', '-X', 'Y', 'Z']))
