# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_urllib.py
# case: QuotingTests_test_quoting_space

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    result = urllib.parse.quote(' ')
    self.assertEqual(result, hexescape(' '), 'using quote(): %r != %r' % (result, hexescape(' ')))
    result = urllib.parse.quote_plus(' ')
    self.assertEqual(result, '+', 'using quote_plus(): %r != +' % result)
    given = 'a b cd e f'
    expect = given.replace(' ', hexescape(' '))
    result = urllib.parse.quote(given)
    self.assertEqual(expect, result, 'using quote(): %r != %r' % (expect, result))
    expect = given.replace(' ', '+')
    result = urllib.parse.quote_plus(given)
    self.assertEqual(expect, result, 'using quote_plus(): %r != %r' % (expect, result))
