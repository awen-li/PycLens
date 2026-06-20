# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_urllib.py
# case: UnquotingTests_test_unquoting_badpercent

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    given = '%xab'
    expect = given
    result = urllib.parse.unquote(given)
    self.assertEqual(expect, result, 'using unquote(): %r != %r' % (expect, result))
    given = '%x'
    expect = given
    result = urllib.parse.unquote(given)
    self.assertEqual(expect, result, 'using unquote(): %r != %r' % (expect, result))
    given = '%'
    expect = given
    result = urllib.parse.unquote(given)
    self.assertEqual(expect, result, 'using unquote(): %r != %r' % (expect, result))
    given = '%xab'
    expect = bytes(given, 'ascii')
    result = urllib.parse.unquote_to_bytes(given)
    self.assertEqual(expect, result, 'using unquote_to_bytes(): %r != %r' % (expect, result))
    given = '%x'
    expect = bytes(given, 'ascii')
    result = urllib.parse.unquote_to_bytes(given)
    self.assertEqual(expect, result, 'using unquote_to_bytes(): %r != %r' % (expect, result))
    given = '%'
    expect = bytes(given, 'ascii')
    result = urllib.parse.unquote_to_bytes(given)
    self.assertEqual(expect, result, 'using unquote_to_bytes(): %r != %r' % (expect, result))
    self.assertRaises((TypeError, AttributeError), urllib.parse.unquote_to_bytes, None)
    self.assertRaises((TypeError, AttributeError), urllib.parse.unquote_to_bytes, ())
