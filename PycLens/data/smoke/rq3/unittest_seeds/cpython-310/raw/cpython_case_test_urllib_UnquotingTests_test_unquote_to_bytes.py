# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_urllib.py
# case: UnquotingTests_test_unquote_to_bytes

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    given = 'br%C3%BCckner_sapporo_20050930.doc'
    expect = b'br\xc3\xbcckner_sapporo_20050930.doc'
    result = urllib.parse.unquote_to_bytes(given)
    self.assertEqual(expect, result, 'using unquote_to_bytes(): %r != %r' % (expect, result))
    result = urllib.parse.unquote_to_bytes('漢%C3%BC')
    expect = b'\xe6\xbc\xa2\xc3\xbc'
    self.assertEqual(expect, result, 'using unquote_to_bytes(): %r != %r' % (expect, result))
    given = b'%A2%D8ab%FF'
    expect = b'\xa2\xd8ab\xff'
    result = urllib.parse.unquote_to_bytes(given)
    self.assertEqual(expect, result, 'using unquote_to_bytes(): %r != %r' % (expect, result))
    given = b'%A2\xd8ab%FF'
    expect = b'\xa2\xd8ab\xff'
    result = urllib.parse.unquote_to_bytes(given)
    self.assertEqual(expect, result, 'using unquote_to_bytes(): %r != %r' % (expect, result))
