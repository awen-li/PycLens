# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_urllib.py
# case: QuotingTests_test_quote_plus_with_unicode

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    given = '¢Ø ÿ'
    expect = '%A2%D8+%FF'
    result = urllib.parse.quote_plus(given, encoding='latin-1')
    self.assertEqual(expect, result, 'using quote_plus(): %r != %r' % (expect, result))
    given = 'ab漢字 cd'
    expect = 'ab%3F%3F+cd'
    result = urllib.parse.quote_plus(given, encoding='latin-1', errors='replace')
    self.assertEqual(expect, result, 'using quote_plus(): %r != %r' % (expect, result))
