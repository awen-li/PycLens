# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_urllib.py
# case: UnquotingTests_test_unquote_with_unicode

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    given = 'br%C3%BCckner_sapporo_20050930.doc'
    expect = 'brückner_sapporo_20050930.doc'
    result = urllib.parse.unquote(given)
    self.assertEqual(expect, result, 'using unquote(): %r != %r' % (expect, result))
    result = urllib.parse.unquote(given, encoding=None, errors=None)
    self.assertEqual(expect, result, 'using unquote(): %r != %r' % (expect, result))
    result = urllib.parse.unquote('br%FCckner_sapporo_20050930.doc', encoding='latin-1')
    expect = 'brückner_sapporo_20050930.doc'
    self.assertEqual(expect, result, 'using unquote(): %r != %r' % (expect, result))
    given = '%E6%BC%A2%E5%AD%97'
    expect = '漢字'
    result = urllib.parse.unquote(given)
    self.assertEqual(expect, result, 'using unquote(): %r != %r' % (expect, result))
    given = '%F3%B1'
    expect = '�'
    result = urllib.parse.unquote(given)
    self.assertEqual(expect, result, 'using unquote(): %r != %r' % (expect, result))
    result = urllib.parse.unquote(given, errors='replace')
    self.assertEqual(expect, result, 'using unquote(): %r != %r' % (expect, result))
    given = '%F3%B1'
    expect = ''
    result = urllib.parse.unquote(given, errors='ignore')
    self.assertEqual(expect, result, 'using unquote(): %r != %r' % (expect, result))
    result = urllib.parse.unquote('漢%C3%BC')
    expect = '漢ü'
    self.assertEqual(expect, result, 'using unquote(): %r != %r' % (expect, result))
    result = urllib.parse.unquote('漢%FC', encoding='latin-1')
    expect = '漢ü'
    self.assertEqual(expect, result, 'using unquote(): %r != %r' % (expect, result))
