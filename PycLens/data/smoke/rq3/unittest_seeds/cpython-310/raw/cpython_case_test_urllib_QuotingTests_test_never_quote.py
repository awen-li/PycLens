# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_urllib.py
# case: QuotingTests_test_never_quote

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    do_not_quote = ''.join(['ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz', '0123456789', '_.-~'])
    result = urllib.parse.quote(do_not_quote)
    self.assertEqual(do_not_quote, result, 'using quote(): %r != %r' % (do_not_quote, result))
    result = urllib.parse.quote_plus(do_not_quote)
    self.assertEqual(do_not_quote, result, 'using quote_plus(): %r != %r' % (do_not_quote, result))
