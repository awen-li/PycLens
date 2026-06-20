# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_urlparse.py
# case: UrlParseTestCase_test_unparse_parse

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    str_cases = ['Python', './Python', 'x-newscheme://foo.com/stuff', 'x://y', 'x:/y', 'x:/', '/']
    bytes_cases = [x.encode('ascii') for x in str_cases]
    for u in str_cases + bytes_cases:
        self.assertEqual(urllib.parse.urlunsplit(urllib.parse.urlsplit(u)), u)
        self.assertEqual(urllib.parse.urlunparse(urllib.parse.urlparse(u)), u)
