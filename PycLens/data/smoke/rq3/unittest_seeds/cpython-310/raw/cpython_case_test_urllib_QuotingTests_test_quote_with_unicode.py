# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_urllib.py
# case: QuotingTests_test_quote_with_unicode

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    given = '¢Øabÿ'
    expect = '%C2%A2%C3%98ab%C3%BF'
    result = urllib.parse.quote(given)
    self.assertEqual(expect, result, 'using quote(): %r != %r' % (expect, result))
    result = urllib.parse.quote(given, encoding=None, errors=None)
    self.assertEqual(expect, result, 'using quote(): %r != %r' % (expect, result))
    given = '¢Øabÿ'
    expect = '%A2%D8ab%FF'
    result = urllib.parse.quote(given, encoding='latin-1')
    self.assertEqual(expect, result, 'using quote(): %r != %r' % (expect, result))
    given = '漢字'
    expect = '%E6%BC%A2%E5%AD%97'
    result = urllib.parse.quote(given)
    self.assertEqual(expect, result, 'using quote(): %r != %r' % (expect, result))
    given = '漢字'
    self.assertRaises(UnicodeEncodeError, urllib.parse.quote, given, encoding='latin-1')
    given = '漢字'
    expect = '%3F%3F'
    result = urllib.parse.quote(given, encoding='latin-1', errors='replace')
    self.assertEqual(expect, result, 'using quote(): %r != %r' % (expect, result))
    given = '漢字'
    expect = '%26%2328450%3B%26%2323383%3B'
    result = urllib.parse.quote(given, encoding='latin-1', errors='xmlcharrefreplace')
    self.assertEqual(expect, result, 'using quote(): %r != %r' % (expect, result))
