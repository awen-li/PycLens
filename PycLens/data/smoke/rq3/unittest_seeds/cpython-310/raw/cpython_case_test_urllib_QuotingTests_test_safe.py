# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_urllib.py
# case: QuotingTests_test_safe

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    quote_by_default = '<>'
    result = urllib.parse.quote(quote_by_default, safe=quote_by_default)
    self.assertEqual(quote_by_default, result, 'using quote(): %r != %r' % (quote_by_default, result))
    result = urllib.parse.quote_plus(quote_by_default, safe=quote_by_default)
    self.assertEqual(quote_by_default, result, 'using quote_plus(): %r != %r' % (quote_by_default, result))
    result = urllib.parse.quote(quote_by_default, safe=b'<>')
    self.assertEqual(quote_by_default, result, 'using quote(): %r != %r' % (quote_by_default, result))
    result = urllib.parse.quote('aüb', encoding='latin-1', safe='ü')
    expect = urllib.parse.quote('aüb', encoding='latin-1', safe='')
    self.assertEqual(expect, result, 'using quote(): %r != %r' % (expect, result))
    result = urllib.parse.quote('aüb', encoding='latin-1', safe=b'\xfc')
    expect = urllib.parse.quote('aüb', encoding='latin-1', safe='')
    self.assertEqual(expect, result, 'using quote(): %r != %r' % (expect, result))
