# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_urlparse.py
# case: UrlParseTestCase_test_parse_qsl_separator

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    parse_qsl_semicolon_cases = [(';', []), (';;', []), (';a=b', [('a', 'b')]), ('a=a+b;b=b+c', [('a', 'a b'), ('b', 'b c')]), ('a=1;a=2', [('a', '1'), ('a', '2')]), (b';', []), (b';;', []), (b';a=b', [(b'a', b'b')]), (b'a=a+b;b=b+c', [(b'a', b'a b'), (b'b', b'b c')]), (b'a=1;a=2', [(b'a', b'1'), (b'a', b'2')])]
    for (orig, expect) in parse_qsl_semicolon_cases:
        with self.subTest(f'Original: {orig!r}, Expected: {expect!r}'):
            result = urllib.parse.parse_qsl(orig, separator=';')
            self.assertEqual(result, expect, 'Error parsing %r' % orig)
            result_bytes = urllib.parse.parse_qsl(orig, separator=b';')
            self.assertEqual(result_bytes, expect, 'Error parsing %r' % orig)
