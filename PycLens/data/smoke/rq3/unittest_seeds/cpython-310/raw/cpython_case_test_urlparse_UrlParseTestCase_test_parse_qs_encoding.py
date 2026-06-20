# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_urlparse.py
# case: UrlParseTestCase_test_parse_qs_encoding

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    result = urllib.parse.parse_qs('key=Ł%E9', encoding='latin-1')
    self.assertEqual(result, {'key': ['Łé']})
    result = urllib.parse.parse_qs('key=Ł%C3%A9', encoding='utf-8')
    self.assertEqual(result, {'key': ['Łé']})
    result = urllib.parse.parse_qs('key=Ł%C3%A9', encoding='ascii')
    self.assertEqual(result, {'key': ['Ł��']})
    result = urllib.parse.parse_qs('key=Ł%E9-', encoding='ascii')
    self.assertEqual(result, {'key': ['Ł�-']})
    result = urllib.parse.parse_qs('key=Ł%E9-', encoding='ascii', errors='ignore')
    self.assertEqual(result, {'key': ['Ł-']})
