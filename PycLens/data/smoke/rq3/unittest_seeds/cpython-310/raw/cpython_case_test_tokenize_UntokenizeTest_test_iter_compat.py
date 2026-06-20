# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_tokenize.py
# case: UntokenizeTest_test_iter_compat

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    u = Untokenizer()
    token = (NAME, 'Hello')
    tokens = [(ENCODING, 'utf-8'), token]
    u.compat(token, iter([]))
    self.assertEqual(u.tokens, ['Hello '])
    u = Untokenizer()
    self.assertEqual(u.untokenize(iter([token])), 'Hello ')
    u = Untokenizer()
    self.assertEqual(u.untokenize(iter(tokens)), 'Hello ')
    self.assertEqual(u.encoding, 'utf-8')
    self.assertEqual(untokenize(iter(tokens)), b'Hello ')
