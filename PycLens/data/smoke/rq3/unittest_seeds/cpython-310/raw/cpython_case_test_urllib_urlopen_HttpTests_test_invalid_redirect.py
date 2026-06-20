# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_urllib.py
# case: urlopen_HttpTests_test_invalid_redirect

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.fakehttp(b'HTTP/1.1 302 Found\nDate: Wed, 02 Jan 2008 03:03:54 GMT\nServer: Apache/1.3.33 (Debian GNU/Linux) mod_ssl/2.8.22 OpenSSL/0.9.7e\nLocation: file://guidocomputer.athome.com:/python/license\nConnection: close\nContent-Type: text/html; charset=iso-8859-1\n', mock_close=True)
    try:
        msg = "Redirection to url 'file:"
        with self.assertRaisesRegex(urllib.error.HTTPError, msg):
            urlopen('http://python.org/')
    finally:
        self.unfakehttp()
