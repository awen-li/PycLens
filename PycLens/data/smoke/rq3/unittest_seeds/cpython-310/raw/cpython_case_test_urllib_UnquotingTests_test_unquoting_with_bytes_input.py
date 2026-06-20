# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_urllib.py
# case: UnquotingTests_test_unquoting_with_bytes_input

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    given = b'blueberryjam'
    expect = 'blueberryjam'
    result = urllib.parse.unquote(given)
    self.assertEqual(expect, result, 'using unquote(): %r != %r' % (expect, result))
    given = b'bl\xc3\xa5b\xc3\xa6rsyltet\xc3\xb8y'
    expect = 'blåbærsyltetøy'
    result = urllib.parse.unquote(given)
    self.assertEqual(expect, result, 'using unquote(): %r != %r' % (expect, result))
    given = b'bl%c3%a5b%c3%a6rsyltet%c3%b8j'
    expect = 'blåbærsyltetøj'
    result = urllib.parse.unquote(given)
    self.assertEqual(expect, result, 'using unquote(): %r != %r' % (expect, result))
