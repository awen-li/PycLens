# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_urllib.py
# case: urlopen_HttpTests_test_userpass_inurl

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.fakehttp(b'HTTP/1.0 200 OK\r\n\r\nHello!')
    try:
        fp = urlopen('http://user:pass@python.org/')
        self.assertEqual(fp.readline(), b'Hello!')
        self.assertEqual(fp.readline(), b'')
        self.assertEqual(fp.geturl(), 'http://user:pass@python.org/')
        self.assertEqual(fp.getcode(), 200)
    finally:
        self.unfakehttp()
