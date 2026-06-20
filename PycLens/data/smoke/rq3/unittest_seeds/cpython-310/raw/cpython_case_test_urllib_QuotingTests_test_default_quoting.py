# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_urllib.py
# case: QuotingTests_test_default_quoting

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    should_quote = [chr(num) for num in range(32)]
    should_quote.append('<>#%"{}|\\^[]`')
    should_quote.append(chr(127))
    should_quote = ''.join(should_quote)
    for char in should_quote:
        result = urllib.parse.quote(char)
        self.assertEqual(hexescape(char), result, 'using quote(): %s should be escaped to %s, not %s' % (char, hexescape(char), result))
        result = urllib.parse.quote_plus(char)
        self.assertEqual(hexescape(char), result, 'using quote_plus(): %s should be escapes to %s, not %s' % (char, hexescape(char), result))
    del should_quote
    partial_quote = 'ab[]cd'
    expected = 'ab%5B%5Dcd'
    result = urllib.parse.quote(partial_quote)
    self.assertEqual(expected, result, 'using quote(): %r != %r' % (expected, result))
    result = urllib.parse.quote_plus(partial_quote)
    self.assertEqual(expected, result, 'using quote_plus(): %r != %r' % (expected, result))
