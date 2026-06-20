# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_tokenize.py
# case: UntokenizeTest_test_backslash_continuation

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    u = Untokenizer()
    u.prev_row = 1
    u.prev_col = 1
    u.tokens = []
    u.add_whitespace((2, 0))
    self.assertEqual(u.tokens, ['\\\n'])
    u.prev_row = 2
    u.add_whitespace((4, 4))
    self.assertEqual(u.tokens, ['\\\n', '\\\n\\\n', '    '])
    TestRoundtrip.check_roundtrip(self, 'a\n  b\n    c\n  \\\n  c\n')
