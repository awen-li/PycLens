# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_argparse.py
# case: TestAddSubparsers_test_parse_args

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertEqual(self.parser.parse_args('0.5 1 b -w 7'.split()), NS(foo=False, bar=0.5, w=7, x='b'))
    self.assertEqual(self.parser.parse_args('0.25 --foo 2 -y 2 3j -- -1j'.split()), NS(foo=True, bar=0.25, y='2', z=[3j, -1j]))
    self.assertEqual(self.parser.parse_args('--foo 0.125 1 c'.split()), NS(foo=True, bar=0.125, w=None, x='c'))
    self.assertEqual(self.parser.parse_args('-1.5 3 11 -- a --foo 7 -- b'.split()), NS(foo=False, bar=-1.5, t=11, u=['a', '--foo', '7', '--', 'b']))
