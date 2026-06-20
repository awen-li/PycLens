# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_urlparse.py
# case: UrlParseTestCase_test_urlsplit_normalization

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    illegal_chars = '/:#?@'
    hex_chars = {'{:04X}'.format(ord(c)) for c in illegal_chars}
    denorm_chars = [c for c in map(chr, range(128, sys.maxunicode)) if hex_chars & set(unicodedata.decomposition(c).split()) and c not in illegal_chars]
    self.assertIn('℀', denorm_chars)
    self.assertIn('＃', denorm_chars)
    urllib.parse.urlsplit('http://プ:80')
    with self.assertRaises(ValueError):
        urllib.parse.urlsplit('http://プ︓80')
    for scheme in ['http', 'https', 'ftp']:
        for netloc in ['netloc{}false.netloc', 'n{}user@netloc']:
            for c in denorm_chars:
                url = '{}://{}/path'.format(scheme, netloc.format(c))
                with self.subTest(url=url, char='{:04X}'.format(ord(c))):
                    with self.assertRaises(ValueError):
                        urllib.parse.urlsplit(url)
