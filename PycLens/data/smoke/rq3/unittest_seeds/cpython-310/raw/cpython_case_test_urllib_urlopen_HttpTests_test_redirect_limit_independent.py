# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_urllib.py
# case: urlopen_HttpTests_test_redirect_limit_independent

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for i in range(FancyURLopener().maxtries):
        self.fakehttp(b'HTTP/1.1 302 Found\nLocation: file://guidocomputer.athome.com:/python/license\nConnection: close\n', mock_close=True)
        try:
            self.assertRaises(urllib.error.HTTPError, urlopen, 'http://something')
        finally:
            self.unfakehttp()
