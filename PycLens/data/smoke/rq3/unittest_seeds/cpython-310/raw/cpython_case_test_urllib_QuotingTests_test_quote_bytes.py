# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_urllib.py
# case: QuotingTests_test_quote_bytes

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    given = b'\xa2\xd8ab\xff'
    expect = '%A2%D8ab%FF'
    result = urllib.parse.quote(given)
    self.assertEqual(expect, result, 'using quote(): %r != %r' % (expect, result))
    self.assertRaises(TypeError, urllib.parse.quote, given, encoding='latin-1')
    result = urllib.parse.quote_from_bytes(given)
    self.assertEqual(expect, result, 'using quote_from_bytes(): %r != %r' % (expect, result))
