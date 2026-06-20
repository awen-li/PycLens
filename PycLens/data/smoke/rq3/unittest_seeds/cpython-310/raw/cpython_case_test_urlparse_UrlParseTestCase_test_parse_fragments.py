# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_urlparse.py
# case: UrlParseTestCase_test_parse_fragments

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    tests = (('http:#frag', 'path', 'frag'), ('//example.net#frag', 'path', 'frag'), ('index.html#frag', 'path', 'frag'), (';a=b#frag', 'params', 'frag'), ('?a=b#frag', 'query', 'frag'), ('#frag', 'path', 'frag'), ('abc#@frag', 'path', '@frag'), ('//abc#@frag', 'path', '@frag'), ('//abc:80#@frag', 'path', '@frag'), ('//abc#@frag:80', 'path', '@frag:80'))
    for (url, attr, expected_frag) in tests:
        for func in (urllib.parse.urlparse, urllib.parse.urlsplit):
            if attr == 'params' and func is urllib.parse.urlsplit:
                attr = 'path'
            with self.subTest(url=url, function=func):
                result = func(url, allow_fragments=False)
                self.assertEqual(result.fragment, '')
                self.assertTrue(getattr(result, attr).endswith('#' + expected_frag))
                self.assertEqual(func(url, '', False).fragment, '')
                result = func(url, allow_fragments=True)
                self.assertEqual(result.fragment, expected_frag)
                self.assertFalse(getattr(result, attr).endswith(expected_frag))
                self.assertEqual(func(url, '', True).fragment, expected_frag)
                self.assertEqual(func(url).fragment, expected_frag)
