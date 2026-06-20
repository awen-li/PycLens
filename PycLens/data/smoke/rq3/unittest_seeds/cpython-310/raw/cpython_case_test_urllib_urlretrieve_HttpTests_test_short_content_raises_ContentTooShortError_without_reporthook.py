# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_urllib.py
# case: urlretrieve_HttpTests_test_short_content_raises_ContentTooShortError_without_reporthook

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.addCleanup(urllib.request.urlcleanup)
    self.fakehttp(b'HTTP/1.1 200 OK\nDate: Wed, 02 Jan 2008 03:03:54 GMT\nServer: Apache/1.3.33 (Debian GNU/Linux) mod_ssl/2.8.22 OpenSSL/0.9.7e\nConnection: close\nContent-Length: 100\nContent-Type: text/html; charset=iso-8859-1\n\nFF\n')
    with self.assertRaises(urllib.error.ContentTooShortError):
        try:
            urllib.request.urlretrieve(support.TEST_HTTP_URL)
        finally:
            self.unfakehttp()
